- Супер базовая последовательность действий для создания репозитория:
    
**Create a new repository on the command line**
    
    
    echo "# ohlala" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/edirab/ohlala.git
    git push -u origin main

**…or push an existing repository from the command line**

    git remote add origin https://github.com/edirab/ohlala.git
    git branch -M main
    git push -u origin main

NB: Вот это `-M`нужно только для переименования `master` в `main` 
 
    With a -m or -M option, <oldbranch> will be renamed to <newbranch>. 
    If <oldbranch> had a corresponding reflog, it is renamed to match <newbranch>, 
    and a reflog entry is created to remember the branch renaming. 
    If <newbranch> exists, -M must be used to force the rename to happen.


- Переключение нармального отображения кириллицы в консоли:


    git config --local core.quotepath false

- Создать новую ветвь и переключиться на неё:


    git branch new_branch
    git checkout new_branch
или же

    git checkout -b new_branch


- Отправить ветвь в удалённый репозиторий:


    git push origin -u master
    git push origin new_branch
    git push https://github.com/edirab/Lovely-Notebooks.git new_branch
    
Ключ `-u` (`--set-upstream`) делает текущую ветку по умоланию для публикации изменений

- Отменить добавление файлов к отслеживаемым:


	git reset
	git reset <file1> <file2> ...


- Удалить последний коммит. При этом все изменения станут как  "Changes to be committed"


	git reset --soft HEAD~1
	
- Переключиться на коммит просто чтобы посмотреть:


	git checkout <hash-value>
	
- Извлечь ВЕСЬ репозиторий и перетереть нежелательные изменения в рабочей директории:


	git fetch --all
	get reset --hard origin/master
	
- Посмотреть все имеющиеся ветви:


	git branch
	
- Посмотреть все url, к которым привязан локальный репозиторий


	git remote -v