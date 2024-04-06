import webbrowser # Hàm có sẵn trong python để mở một link

class Playlist:
    def __init__ (self, name, description, videos):
        self.name = name
        self.description = description
        self.videos = videos

class Video:
    def __init__(self, title, link): # Hàm khởi tạo bắt buộc các thuộc tính của Object
        self.title = title
        self.link = link
        self.seen = False
    def open(self):
        webbrowser.open(self.link)
        self.seen = True

# Input 1 video
def video_input():
    title_input = input("Nhập tên Video: ") + "\n"
    link_input = input("Nhập URL: ") + "\n"
    vid_input = Video(title_input, link_input)
    return vid_input

# Input nhiều video
def videos_input():
    list_input = []
    total_vid = int(input("Nhập số lượng Videos: "))
    for i in range(total_vid):
        print("-----")
        print("Nhập thông tin Video ", "|", i+1, "|")
        vids_input = video_input()
        list_input.append(vids_input)
    return list_input

# Output 1 video
def video_output(vid_output):
    print("-----")
    print("Title Video: ", vid_output.title, end="") # Bỏ xuống dòng trong hàm print do hàm realine đã mặc định có xuống dòng nếu print xuống dòng -> xuống 2 dòng
    print("Link Video: ", vid_output.link, end="")

# Output nhiều video
def videos_output(vids_output):
    # Vòng lặp chạy hết số lượng của danh sách truyền vào biến clips_input trong hàm videos_input và xuất từng giá trị của danh sách theo index
    for i in range (len(vids_output)):
        print("Video" + str(i+1) + ":")
        video_output(vids_output[i]) 

# Hàm phụ ghi từng video vào file data.txt
def write_video_data (vids_data, data_file):
        data_file.write(vids_data.title)# Xuống dòng sau khi ghi dữ liệu
        data_file.write(vids_data.link) 

# Ghi toàn bộ dữ liệu vào file data.txt
def write_videos_data(vids_write,file_write_videos):
    total_clip = len(vids_write)
    file_write_videos.write(str(total_clip) + "\n") # Ghi số lượng video vào file data
    # Vòng lặp chạy hết số lượng của danh sách truyển vào biến clips_write 
    for i in range (total_clip):
        write_video_data (vids_write[i], file_write_videos)

# Hàm phụ đọc từng video trong file data.txt
def read_video_data(file_video):
    title_read = file_video.readline()
    link_read = file_video.readline()
    list_data = Video(title_read, link_read)
    return list_data
   
# Đọc dữ liệu từ file data.txt
def read_videos_data(file_read_videos):
    list_read = []
    total_read = file_read_videos.readline() # Đọc dòng đầu tiền chính là số lượng video và ghi vào biến
    for i in range (int(total_read)):
        list_data = read_video_data(file_read_videos)
        list_read.append(list_data)
    return list_read
    
def playlist_input():
    playlist_name = input("Nhập tên Playlist: ") + "\n"
    playlist_des = input("Nhập description: ") + "\n"
    playlist_video = videos_input()
    playlist = Playlist(playlist_name, playlist_des, playlist_video)
    return playlist
    
def write_playlist_data(playlist_write):
    with open("data.txt", "w") as file_write_playlist:
        file_write_playlist.write(playlist_write.name)
        file_write_playlist.write(playlist_write.description)
        write_videos_data(playlist_write.videos, file_write_playlist)
    print(" Ghi dữ liệu thành công ! ")

def read_playlist_data(file_playlist):
    with open("data.txt", "r") as file_read_playlist:
        playlist_title = file_read_playlist.readline()
        playlist_dis = file_read_playlist.readline()
        playlist_videos = read_videos_data(file_read_playlist)
        playlist_read = Playlist(playlist_title, playlist_dis, playlist_videos)
    return playlist_read

def playlist_output(pls_output):
    print("----- ")
    print("Tên Playlist" , pls_output.name, end="")
    print("Tên Playlist: " , pls_output.description, end="")
    videos_output(pls_output.videos)

def menu():
    print("-------CHỌN CHỨC NĂNG--------")
    print("|Chọn '1': Tạo Playlist     |")
    print("|Chọn '2': Hiển thị Playlist|")
    print("|Chọn '3': Mở Video         |")
    print("|Chọn '4': Thêm Video       |")
    print("|Chọn '5': Sửa Video        |")
    print("|Chọn '6': Xóa Video        |")
    print("|Chọn '7': Sửa Playlist     |")
    print("|Chọn '8': Lưu và Thoát     |")
    print("-----------------------------")

# Hàm giới hạn Lựa chọn của User
def select_in_range(prompt, min, max):
    choice_range = input(prompt)
    while not choice_range.isdigit() or int(choice_range) < min or int(choice_range) > max:
        choice_range = input(prompt)
    choice_range = int(choice_range)
    return choice_range
# Hàm chạy Link
def play_video(play):
    videos_output(play.videos)
    total_videos = len(play.videos)
    choice_play = select_in_range("Chọn video(1," + str(total_videos) + ")" , 1, total_videos)
    print("Mở video: " + play.videos[choice_play-1].title + " - " + play.videos[choice_play-1].link, end = "")
    play.videos[choice_play-1].open()

# Hàm thêm Video
def add_video(playlist_add):
    new_videos_title = input("Nhập tên video mới: ") + "\n"
    new_video_link = input("Nhập URL video mới: ") + "\n"
    new_video = Video(new_videos_title, new_video_link)
    playlist_add.videos.appen(new_video)
    return playlist_add    

# Hàm sử Playlist
def edit_playlist(play_edit):
    print("1. Tên")
    print("2. Description")
    choice_edit = select_in_range("Nhập thuộc tính cần sửa: ", 1, 2)
    if choice_edit == 1:
        new_playlist_name = input("Nhập tên mới của Playlist: ") + "\n"
        play_edit.name = new_playlist_name
        print("Đã cập nhật.")
        return play_edit
    if choice_edit == 2:
        new_playliets_des = input("Nhập Description mới của Playlist: ") + "\n"
        play_edit.description = new_playliets_des
        print("Đã cập nhật.")
        return play_edit
    
# Hàm xóa Video
def remove_video(vid_del):
    videos_output(vid_del.videos)
    choice_del = select_in_range("Nhập Video cần xóa: ", 1, len(vid_del.videos))
    del vid_del.videos[choice_del-1]
    return vid_del

#Hàm sửa Video
def edit_video(vid_edit):
    videos_output(vid_edit)
    choice_vid = select_in_range("Nhập Video cần sửa:", 1, len(vid_edit.videos))
    video_output(choice_vid)
    choice_edit = select_in_range("Nhập thông tin cần sửa:", 1, len(choice_vid))
    if choice_edit == 1:
        new_title_edit = input("Nhập Tên mới của Video: ") + "\n"
        choice_vid.title = new_title_edit
        print("Đã đổi tên")
        return new_title_edit
    if choice_edit == 2:
        new_link_edit = input("Nhập Link mới của Video: ") + "\n"
        choice_vid.link = new_link_edit
        print("Đã đổi link")
        return new_link_edit
    
def main():
    # vids = videos_input()
    # write_videos_data (vids)
    # vids = read_videos_data()
    # videos_output(vids)

    # playlist = playlist_input()
    # write_playlist_data(playlist)
    # playlist = read_playlist _data()
    # playlist_output(playlist)

    try:
        playlist = read_playlist_data()
        print("Chạy dữ liệu thành công !")
    except:
        print("Chào mừng bạn đến với chương trình !")
    while True:
        menu()
        choice = select_in_range("Vui lòng chọn (1-7): ", 1, 7)
        if choice == 1:
            playlist = playlist_input()
            input("\nBấm phím bất kỳ để tiếp tục.")
        elif choice == 2:
            playlist_output(playlist)
            input("\nBấm phím bất kỳ để tiếp tục.")
        elif choice == 3:
            play_video(playlist)
            input("\nBấm phím bất kỳ để tiếp tục.")
        elif choice == 4:
            playlist = add_video(playlist)
            input("\nBấm phím bất kỳ để tiếp tục.")
        elif choice == 5:
            playlist = edit_video(playlist)
            input("\nBấm phím bất kỳ để tiếp tục.")
        elif choice == 6:
            playlist = remove_video(playlist)
            input("\nBấm phím bất kỳ để tiếp tục.")
        elif choice == 7:
            playlist = edit_playlist(playlist)
            input("\nBấm phím bất kỳ để tiếp tục.")
        elif choice == 8:
            write_playlist_data(playlist)
            input("\nBấm phím bất kỳ để tiếp tục.")
            break
        else:
            print("Vui lòng chọn (1-8)")
            break
main()

# import pygame

# pygame.init()
# screen = pygame.display.set_mode((600, 400))
# pygame.display.set_caption("Pygame App")
# running = True
# BLACK = (0, 0, 0)
# clock = pygame.time.Clock()

# while running:
#     clock.tick(60)
#     screen.fill(BLACK)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         pygame.display.flip()

# pygame.quit()
