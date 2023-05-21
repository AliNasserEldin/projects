# SecureVault : password manager terminal application

#### Video Demo:  https://youtu.be/LMB450Z3kmI
---
#### Description:
The password manager terminal app is an incredibly useful tool for managing all of your online passwords in one secure location. With six intuitive methods, this app makes it easy to add, reveal, update, and delete passwords as needed.

- The first method **add** is for adding passwords hashed, which means that the app encrypts the password before storing it in its database. This ensures that even if someone gains access to the database, they won't be able to read the passwords without the encryption key. Additionally, this method doesn't allow duplicated records, so users can be sure that each password is unique.

- The second method **reveal_one** is for revealing a password after decrypting it. This is useful when users need to access a website or service and don't remember their password. By using this method, they can quickly retrieve their password without having to reset it.

- The third method **reveal_all** reveals all passwords after decrypting them. This is useful for users who want to review all of their stored passwords or need to export them for backup purposes.

- The fourth method **delete_one** allows users to delete a password from the database. If they no longer need a particular password or want to remove it for security reasons, they can use this method to delete it.

- The fifth method **delete_all** deletes all passwords from the database. This is useful if users want to start fresh with new passwords or are no longer using the app.

- the sixth method is **about** which reviews a few lines introducing the program to the user explaining
why who useful this app is.

- Finally, the seventh method **update** allows users to update an existing password. If they need to change a password for security reasons, they can use this method to update it in the database.

### additional methods
#### the app also got some methods which serve the six methods  above :
- **is_exist** : returns true if record already exists in file and false other ways,
this method works before adding a record to the file to make sure that there is no duplicates
or conflicts in emails and passwords and before deleting to make sure the specified record to delete is
in the passwords file
- **choose** : takes number of choices as argument and keeps prompting the user to
  choose number from 1 to number of choices and if he chooses a wrong number
  the method prints an error message
---
overall, this password manager terminal app provides users with powerful tools for managing their passwords securely and efficiently. With these six methods at their disposal, they can easily add, reveal, delete, and update their passwords as needed.
