import libtorrent as lt

def create_magnet_link(torrent_file_path):
    info = lt.torrent_info(torrent_file_path)
    hash = str(info.info_hash())
    name = info.name()
    magnet_link = f"magnet:?xt=urn:btih:{hash}&dn={name}"
    return magnet_link

# Usage
torrent_file_path = "/path/to/your/torrent/file.torrent"
magnet_link = create_magnet_link(torrent_file_path)
print(magnet_link)