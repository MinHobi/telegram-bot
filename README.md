# Telegram Forwarder

Bot Telegram Python chạy Python3 tự động forward file từ 1 hay nhiều trò chuyện này sang các trò chuyện khác.

## Cấu hình Bot

Telegram Forwarder chỉ hỗ trợ Python 3.9 trở lên.

### Cấu hình

Để bot hoạt động cần cấu hình 2 file `.env` và `chat_list.json`.

### `.env`

Thay bằng cách tham số của bạn:

-   `BOT_TOKEN` - Telegram bot token. Chat với [@BotFather](https://t.me/BotFather) để lấy được nó

-   `OWNER_ID` - ID chat của bạn.

-   `REMOVE_TAG` - đặt thành `True` nếu bạn muốn xóa tag ("Forwarded from xxxxx") từ tin nhắn chuyển tiếp.

#### `chat_list.json`

File này chứa danh sách các cuộc trờ chuyện nguồn và đích để chuyển tiếp tin nhắn.

```json
[
    {
        "source": [-10012345678],
        "destination": [-10011111111, "-10022222222#123456"]
    }
]
```

-   `source` - Danh sách ID chat của trò chuyện nguồn để chuyển tiếp tin nhắn từ đó. Nó có thể là group hoặc channel.

-   `destination` - Danh sách ID chat của trò chuyện đích để chuyển tiếp tin nhắn tới. Nó có thể là group hoặc channel.
    > Destenation hỗ trợ Topics chat. Bạn có thể sử dụng chuỗi `#topicID` để chuyển tiếp đến topic cụ thể. Ví dụ: `[-10011111111, "-10022222222#123456"]`. Nó sẽ chuyển tiếp tin nhắn đến trò chuyện `-10022222222` với topic `123456` và trò chuyện `-10011111111` .

### Python dependencies

Cài đặt tất cả các package Python cần thiết:

```shell
pip3 install -r requirements.txt
```

## Starting The Bot

Sau khi thiết lập xong cấu hình, chỉ cần chạy:

```shell
python -m forwarder
```


