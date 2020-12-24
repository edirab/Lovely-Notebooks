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

- Узнать **все текущие настройки** git:


	git config --list

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
	
- Сохранить пароль чтобы не вводить каждый раз


	git config --global credential.helper wincred


Пароль будет сохранён в Credential Manager, по русски Диспетчер учетных данных (Панель управления\Все элементы панели управления\Диспетчер учетных данных)

- https://docs.github.com/en/free-pro-team@latest/github/using-git/changing-a-remotes-url




- Как (легко удалить)[https://rtyley.github.io/bfg-repo-cleaner/] из истории git ненужные файлы и папки:


	java -jar bfg-1.13.1.jar --delete-folders slprj
	java -jar bfg-1.13.1.jar -D *.slxc
	java -jar bfg-1.13.1.jar -D *.autosave
	
	
<details>
<summary>Пример вывода</summary>
```shell
	E:\University\11sem\Курсовой_2>java -jar bfg-1.13.1.jar -D *.autosave

	Using repo : E:\University\11sem\Курсовой_2\.git

	Found 34 objects to protect
	Found 2 commit-pointing refs : HEAD, refs/heads/master

	Protected commits
	-----------------

	These are your protected commits, and so their contents will NOT be altered:

	 * commit c9f6ec2c (protected by 'HEAD')

	Cleaning
	--------

	Found 9 commits
	Cleaning commits:       100% (9/9)
	Cleaning commits completed in 154 ms.

	Updating 1 Ref
	--------------

			Ref                 Before     After
			---------------------------------------
			refs/heads/master | c9f6ec2c | c6542536

	Updating references:    100% (1/1)
	...Ref update completed in 13 ms.

	Commit Tree-Dirt History
	------------------------

			Earliest      Latest
			|                  |
			 . . . . .  . D m m

			D = dirty commits (file tree fixed)
			m = modified commits (commit message or parents changed)
			. = clean commits (no changes to file tree)

									Before     After
			-------------------------------------------
			First modified commit | b5bf9576 | 38aab685
			Last dirty commit     | b5bf9576 | 38aab685

	Deleted files
	-------------

			Filename               Git id
			-----------------------------------------
			forward.slx.autosave | 3ba09fa7 (23,7 KB)


	In total, 5 object ids were changed. Full details are logged here:

			E:\University\11sem\Курсовой_2.bfg-report\2020-12-24\23-53-42

	BFG run is complete! When ready, run: git reflog expire --expire=now --all && git gc --prune=now --aggressive
```
</details>

