### Использование подсистемы Linux для Windows

1. Для начала потребуется Microsoft Store (в Win 10 LTSC его нет по умолчанию). Проблему решает
[репозиторий](https://github.com/kkkgo/LTSC-Add-MicrosoftStore).

2. Следуя официальному руководству, [включаем WSL2 ](https://docs.microsoft.com/ru-ru/windows/wsl/install-win10). В командной строке, запушенной от администратора:

    ```
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    wsl --set-default-version 2
    ```
    Могут возникнуть вопросы с включённым/отключённым гипервизором (Hyper V).
    
3. Скачиваем/устанавливаем любимый linux-дистрибутив из `Microsoft Store`


Диски находятся в папке `/mnt/`:

	/mnt/e/Работа/НПО Варя/zxing-cpp-opencv/research/tcp_and_sockets/v1

*****

- Запуск процесса в фоне:


	./server &
	
- Узнать состояние всех остановленных и выполняемых в фоновом режиме задач в рамках текущей 
сессии терминала можно при помощи утилиты jobs c использованием опции -l:
	
	
	jobs -l
	
	
- В любое время можно вернуть процесс из фонового режима на передний план. Для этого служит команда `fg`:


	fg
	
Если в фоновом режиме выполняется несколько программ, следует также указывать номер. Например:

	fg %1

- В фоновом режиме можно одновременно запускать сразу два, три, четыре процесса и даже больше.
Работая в фоновом режиме, команда все равно продолжает выводить сообщения в терминал, 
из которого была запущена. Для этого она использует потоки stdout и stderr,  которые можно 
закрыть при помощи следующего синтаксиса:


	command > /dev/null 2>&1 &

Здесь `>/dev/null 2>&1` обозначает, что stdout будет перенаправлен на `/dev/null`, а `stderr` — к `stdout`.