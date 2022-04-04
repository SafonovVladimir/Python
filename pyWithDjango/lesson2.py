class CommentFromWebSite():
    '''
    Комментарий с сайта
    '''

    def __init__(self, data, text, likes):
        self.data = data
        self.text = text
        self.likes = int(likes)

    def showComment(self):
        '''
        Вивести коментарій у консоль
        '''
        print(f'\nКоментарій з сайту: \n дата: {self.data}'
              f'\n текст: {self.text}\n кількість лайків: {self.likes}')

    def changeLikes(self):
        '''
        Добавляє 1 лайк
        '''
        self.likes = self.likes + 1

    def changeComments(self, new_text):
        '''
        Зміна коментаря
        '''
        self.text = new_text

new_comment = CommentFromWebSite('04/04/2022', 'First!', '15')
new_comment2 = CommentFromWebSite('05/06/2021', 'Second!', '50')
new_comment3 = CommentFromWebSite('25/03/2020', 'Third!', '40')

# new_comment.showComment()
#
# new_comment3.changeComments('Це новий текст на обєкті 3')
# new_comment3.showComment()

new_comment2.showComment()
new_comment2.changeLikes()
new_comment2.changeLikes()
new_comment2.changeComments('Новий запис другого обєкта')
new_comment2.showComment()
