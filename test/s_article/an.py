import logging

if __name__ == '__main__':
    # Создание логгера
    logger = logging.getLogger('example_logger')
    logger.setLevel(logging.DEBUG)  # Устанавливаем уровень журналирования

    # Создание обработчика для записи в файл
    file_handler = logging.FileHandler('example.log')
    file_handler.setLevel(logging.DEBUG)  # Устанавливаем уровень журналирования для обработчика

    # Определение форматирования для записей в файл
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Добавление обработчика к логгеру
    logger.addHandler(file_handler)

    # Примеры записи сообщений
    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')


# Этот код создает логгер с именем 'example_logger' и устанавливает уровень журналирования на уровне DEBUG. Затем создается обработчик FileHandler, который будет записывать логи в файл с именем 'example.log'.
#
# Уровень журналирования для обработчика также устанавливается на уровне DEBUG, что означает, что все сообщения будут записаны в файл. Вы можете изменить уровень журналирования для обработчика в соответствии с вашими требованиями.
#
# Форматирование сообщений устанавливается для обработчика FileHandler, чтобы определить, как будут выглядеть записи в файле журнала. В этом примере мы используем формат '%(asctime)s - %(name)s - %(levelname)s - %(message)s'.
#
# Наконец, мы добавляем обработчик к логгеру, чтобы он начал записывать сообщения в файл журнала.
