from PyQt5.QtWidgets import (QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QTreeWidget,
                             QLabel, QSlider, QTextEdit,
                             QComboBox, QTreeWidgetItem, 
                             QFileDialog, QFrame)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QTime, Qt, QTimer, QThread, pyqtSignal
import numpy as np
from transformers import BarkModel, AutoProcessor
import torch
import soundfile as sf
from Helper.Stile_Sheets import (button_style_2, Qline_style_L, 
                                 Combo_style_L, QFrame_style_L)
from Helper.MyLabel import MyLabel

np.object = np.dtype('O')
 
class SpeechSynthesisThread(QThread):
    finished_signal = pyqtSignal(str)

    def __init__(self, voice_preset, text_input, save_path):
        super().__init__()
        self.voice_preset = voice_preset
        self.text_input = text_input
        self.save_path = save_path  # Добавляем атрибут save_path

    def run(self):
        # Определяем устройство для использования CPU или GPU
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # Инициализируем обработчик текста и модель для синтеза речи
        processor = AutoProcessor.from_pretrained("suno/bark", device=device)
        model = BarkModel.from_pretrained("suno/bark").to(device)

        # Разделяем текст на фрагменты (например, по предложениям)
        fragments = self.split_text_into_fragments(self.text_input)

        # Создаем пустой массив для аудио
        audio_array = []

        # Генерируем аудио для каждого фрагмента текста
        for fragment in fragments:
            inputs = processor(fragment, voice_preset=self.voice_preset)

            # Перемещаем входные данные на устройство
            inputs_on_device = {key: value.to(device) for key, value in inputs.items() if isinstance(value, torch.Tensor)}

            # Генерируем аудио на устройстве
            fragment_audio = model.generate(**inputs_on_device)

            # Перемещаем аудио на CPU (если оно было сгенерировано на GPU)
            fragment_audio = fragment_audio.cpu().numpy().squeeze()

            audio_array.extend(fragment_audio)

        # Сохраняем аудио в выбранный файл
        sf.write(self.save_path, audio_array, 22050)

        # Отправляем сигнал с путем сохраненного файла
        self.finished_signal.emit(self.save_path)

    def split_text_into_fragments(self, text, max_length=200): 
        fragments = []
        words = text.split()
        current_fragment = ""

        for word in words:
            if len(current_fragment) + len(word) + 1 <= max_length:
                current_fragment += word + " "
            else:
                fragments.append(current_fragment.strip())
                current_fragment = word + " "

        if current_fragment:
            fragments.append(current_fragment.strip())

        return fragments

class AudioPlayer(QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.selected_item = None
        self.selected_audio_path = None
        self.synthesis_thread = None
        self.Tree.itemClicked.connect(self.on_tree_item_clicked)

    # интерфейс
    def init_ui(self):
        main_Layout = QVBoxLayout(self)
        process_layout = QHBoxLayout()
        layout = QHBoxLayout()
        play_layout = QHBoxLayout()
        Сonclusion_play_layout = QHBoxLayout()

        
        # Создание кнопок_____________________________________________________
        self.Process = QPushButton('process')
        self.play_button = QPushButton('play')
        
        self.Process.setStyleSheet(button_style_2)
        self.play_button.setStyleSheet(button_style_2)
        
        self.Process.setFixedSize(40, 20)
        self.play_button.setFixedSize(40, 20)
        
        # Создание комбобоксов_____________________________________________________
        self.presets_lab = QLabel("presets")
        self.presets_lab.setStyleSheet(Qline_style_L)
        self.combobox_presets = QComboBox(self)
        self.combobox_presets.setStyleSheet(Combo_style_L)
        self.load_presets()
        
        self.Tree = QTreeWidget(self)
        self.Tree.setFixedWidth(200)
        
        # Создание TextEdits_____________________________________________________
        self.text_edit_Train = QTextEdit(self)

        # Создание слайдера для перемотки_____________________________________________________
        self.progress_slider = QSlider(Qt.Horizontal)
        self.progress_slider.setRange(0, 0)

        # Создание таймера_____________________________________________________
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        
        # Создание медиаплеера_____________________________________________________
        self.media_player = QMediaPlayer()
        self.current_file_label = QLabel('selected file: none')
        self.current_file_label.setStyleSheet(Qline_style_L)
        self.time_label = QLabel('Time: 00:00 / 00:00')
        self.time_label.setStyleSheet(Qline_style_L)
        
        self.media_IMG_lab_Сonclusion = MyLabel("conclusion")
        self.media_IMG_lab_Сonclusion.setStyleSheet(Qline_style_L)
        self.media_frame_IMG = QFrame(self)
        self.media_frame_IMG.setFrameShape(QFrame.StyledPanel)
        self.media_frame_IMG.setLineWidth(1)
        self.media_frame_layout_IMG = QVBoxLayout(self.media_frame_IMG)
        self.media_frame_layout_IMG.addWidget(self.media_IMG_lab_Сonclusion)
        self.media_frame_IMG.setStyleSheet(QFrame_style_L)
        
        process_layout.addWidget(self.Process)
        process_layout.addStretch()
        process_layout.addWidget(self.presets_lab)
        process_layout.addWidget(self.combobox_presets)
        
        layout.addWidget(self.Tree)
        layout.addWidget(self.text_edit_Train)
        
        play_layout.addWidget(self.play_button)
        play_layout.addWidget(self.time_label)
        play_layout.addWidget(self.progress_slider)
        play_layout.addWidget(self.current_file_label)
        
        Сonclusion_play_layout.addWidget(self.media_frame_IMG)
        
        main_Layout.addLayout(process_layout)
        main_Layout.addLayout(layout)
        main_Layout.addLayout(play_layout)
        main_Layout.addLayout(Сonclusion_play_layout)

        # Обновление времени при перемещении слайдера
        self.progress_slider.sliderMoved.connect(self.set_position)
        
        # подключение кнопок
        self.play_button.clicked.connect(self.Togglet_play)
        self.Process.clicked.connect(self.text_to_speech)

        self.setLayout(main_Layout)
     
    # Обновляем выбранный путь к аудиофайлу при каждом клике на элемент дерева   
    def on_tree_item_clicked(self, item, column):
        self.selected_audio_path = item.text(column)
        self.current_file_label.setText(f'Выбранный файл: {self.selected_audio_path}')

    # добавить аудио в меню "self.Tree"
    def add_audio_to_tree(self, file_path):
        item = QTreeWidgetItem([file_path])
        self.Tree.addTopLevelItem(item)

        self.selected_item = item
        self.selected_audio_path = file_path

    # преобразовать текст в речь
    def text_to_speech(self):
        self.media_IMG_lab_Сonclusion.setText("Генерация")
        voice_preset = self.combobox_presets.currentText()
        text_input = self.text_edit_Train.toPlainText()

        # Получаем путь для сохранения файла
        save_path, _ = QFileDialog.getSaveFileName(self, "Путь для генерации", "", "Wave files (*.wav);;All Files (*)")

        if not save_path:
            return
        
        # Если поток уже запущен, прерываем его выполнение
        if self.synthesis_thread and self.synthesis_thread.isRunning():
            self.synthesis_thread.terminate()

        # Создаем экземпляр потока синтеза речи с указанием save_path
        self.synthesis_thread = SpeechSynthesisThread(voice_preset, text_input, save_path)
        self.synthesis_thread.finished_signal.connect(self.synthesis_thread_finished)

        # Запускаем поток
        self.synthesis_thread.start()

    def synthesis_thread_finished(self, save_path):
        # Обновляем информацию о текущем файле
        self.current_file_label.setText(f'Выбранный файл: {save_path}')

        # Добавляем аудиофайл в дерево
        self.add_audio_to_tree(save_path)
        
        self.media_IMG_lab_Сonclusion.setText("Готово")

    # пресеты голосов для модели (текст - речь)     
    def load_presets(self):
        presets_list = [
            "v2/ru_speaker_0", "v2/ru_speaker_1", "v2/ru_speaker_2", "v2/ru_speaker_3", "v2/ru_speaker_4", "v2/ru_speaker_5", "v2/ru_speaker_6", "v2/ru_speaker_7", "v2/ru_speaker_8", "v2/ru_speaker_9",
            "v2/de_speaker_0", "v2/de_speaker_1", "v2/de_speaker_2", "v2/de_speaker_3", "v2/de_speaker_4", "v2/de_speaker_5", "v2/de_speaker_6", "v2/de_speaker_7", "v2/de_speaker_8", "v2/de_speaker_9",
            "v2/es_speaker_0", "v2/es_speaker_1", "v2/es_speaker_2", "v2/es_speaker_3", "v2/es_speaker_4", "v2/es_speaker_5", "v2/es_speaker_6", "v2/es_speaker_7", "v2/es_speaker_8", "v2/es_speaker_9",
            "v2/fr_speaker_0", "v2/fr_speaker_1", "v2/fr_speaker_2", "v2/fr_speaker_3", "v2/fr_speaker_4", "v2/fr_speaker_5", "v2/fr_speaker_6", "v2/fr_speaker_7", "v2/fr_speaker_8", "v2/fr_speaker_9", 
            "v2/hi_speaker_0", "v2/hi_speaker_1", "v2/hi_speaker_2", "v2/hi_speaker_3", "v2/hi_speaker_4", "v2/hi_speaker_5", "v2/hi_speaker_6", "v2/hi_speaker_7", "v2/hi_speaker_8", "v2/hi_speaker_9",
            "v2/it_speaker_0", "v2/it_speaker_1", "v2/it_speaker_2", "v2/it_speaker_3", "v2/it_speaker_4", "v2/it_speaker_5", "v2/it_speaker_6", "v2/it_speaker_7", "v2/it_speaker_8", "v2/it_speaker_9",
            "v2/ja_speaker_0", "v2/ja_speaker_1", "v2/ja_speaker_2", "v2/ja_speaker_3", "v2/ja_speaker_4", "v2/ja_speaker_5", "v2/ja_speaker_6", "v2/ja_speaker_7", "v2/ja_speaker_8", "v2/ja_speaker_9",
            "v2/ko_speaker_0", "v2/ko_speaker_1", "v2/ko_speaker_2", "v2/ko_speaker_3", "v2/ko_speaker_4", "v2/ko_speaker_5", "v2/ko_speaker_6", "v2/ko_speaker_7", "v2/ko_speaker_8", "v2/ko_speaker_9",
            "v2/pl_speaker_0", "v2/pl_speaker_1", "v2/pl_speaker_2", "v2/pl_speaker_3", "v2/pl_speaker_4", "v2/pl_speaker_5", "v2/pl_speaker_6", "v2/pl_speaker_7", "v2/pl_speaker_8", "v2/pl_speaker_9",
            "v2/pt_speaker_0", "v2/pt_speaker_1", "v2/pt_speaker_2", "v2/pt_speaker_3", "v2/pt_speaker_4", "v2/pt_speaker_5", "v2/pt_speaker_6", "v2/pt_speaker_7", "v2/pt_speaker_8", "v2/pt_speaker_9",
            "v2/tr_speaker_0", "v2/tr_speaker_1", "v2/tr_speaker_2", "v2/tr_speaker_3", "v2/tr_speaker_4", "v2/tr_speaker_5", "v2/tr_speaker_6", "v2/tr_speaker_7", "v2/tr_speaker_8", "v2/tr_speaker_9",
            "v2/zh_speaker_0", "v2/zh_speaker_1", "v2/zh_speaker_2", "v2/zh_speaker_3", "v2/zh_speaker_4", "v2/zh_speaker_5", "v2/zh_speaker_6", "v2/zh_speaker_7", "v2/zh_speaker_8", "v2/zh_speaker_9",
        ]

        self.combobox_presets.addItems(presets_list)

    # Воспроизведение или пауза
    def Togglet_play(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
            self.play_button.setText('Продолжить')
            self.timer.stop()
        else:
            # Используем обновленный путь к выбранному аудиофайлу
            if self.selected_audio_path:
                # Загружаем выбранное аудио в QMediaContent
                media_content = QMediaContent(QUrl.fromLocalFile(self.selected_audio_path))
                self.media_player.setMedia(media_content)

                # Воспроизводим аудио
                self.media_player.play()
                self.play_button.setText('Пауза')
                self.timer.start(1000)  # Запуск таймера каждую секунду
            else:
                # Если ни один элемент не выбран, выводим сообщение или обрабатываем ситуацию по-другому
                print("Не выбран элемент")

    # перемотка аудио
    def set_position(self, position):
        self.media_player.setPosition(position)

    # обновление таймера
    def update_timer(self):
        duration = self.media_player.duration()
        position = self.media_player.position()

        duration_time = QTime(0, 0)
        duration_time = duration_time.addMSecs(duration)

        position_time = QTime(0, 0)
        position_time = position_time.addMSecs(position)

        self.time_label.setText(f'Время: {position_time.toString("mm:ss")} / {duration_time.toString("mm:ss")}')

        # Обновление слайдера
        self.progress_slider.setMaximum(duration)
        self.progress_slider.setValue(position)

