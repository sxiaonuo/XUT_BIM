***ChatGPT永远滴神***

如果登不上github，使用FasterGithub代理
## 远程库操作
**查看分支**
```
git branch -r
```
**删除本地库与某个远程库的链接**
```
git remote remove <remote_name>
```
**与远程库建立连接**
```
git remote add <remote_name> <remote_url>
```
### pull或push 指定远程指定分支
```
git pull origin <远程分支名>:<本地分支名>

git pull origin <远程分支名>

git pull
```

```
git push origin <本地分支名>:<远程分支名>

git push origin <本地分支名>
```
### 合并远程库分支


**`git pull` 相当于 `git fetch` 和 `git merge`**
**git fetch**
```
git fetch XUT_BIM <远程分支名>:<本地分支名>
```
### 删除分支
```
git push <remote_name> --delete <branch_name>
```
## 本地库操作
**查看分支**
```
git branch -v
```
**删除分支**
```
git branch -d master
```
**更改本地分支名**
```
git checkout master
git branch -m master main
```
## 附
将本地分支与远程同名分支相关联
```
git push -u origin <本地分支名>
```
