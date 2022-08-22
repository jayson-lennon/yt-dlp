from .common import InfoExtractor

class MixUploadIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?mixupload\.com/track/.+-(?P<id>[0-9]{7})'
    _TESTS = [{
        'url': 'https://mixupload.com/track/andy-jornee-feat.-victoriya-back-to-1994-6706910',
        'md5': '09be431def9edaaeff85858355761b67',
        'info_dict': {
            'id': '6706910',
            'title': 'Andy Jornee Feat. Victoriya - Back to 1994 (U7EpicTrance) [Universe7]',
            'ext': 'mp3'
        }
    }]

    def _real_extract(self, url):
        video_id = self._match_id(url)
        api_url = f'https://mixupload.com/api2/track/{video_id}/info'
        print(api_url)

        data = self._download_json(api_url, video_id)
        print(data)

        artist = data['track']['artist']
        title = data['track']['title']
        title_post = data['track']['post']
        label = data['track']['label']

        full_title = f'{artist} - {title} ({title_post}) [{label}]'

        download_url = f'https://cdn4.mixupload.com/player/play/{video_id}'

        return {
            'id': video_id,
            'title': full_title,
            'url': download_url,
            'ext': 'mp3'
        }

"""
{
    "status": "ok",
    "track": {
        "id": "6706910",
        "title": "Back to 1994",
        "post": "U7EpicTrance",
        "album": "Back to 1994",
        "artist": "Andy Jornee Feat. Victoriya",
        "label": "Universe7",
        "url": "andy-jornee-feat.-victoriya-back-to-1994-6706910",
        "year": "2022",
        "tags": "7,4,15,19,17",
        "uid": 554253,
        "lock_holder": "0",
        "waveform": "ACFGGHIJKLMTY[[UUUUUVVUUTTUUVWVWVVVXWURRQQUVYZZ\\`[`aacc`eehgfhgegfdhffjighgfhhfhf_Vhnmlnlmieiic]V\\ZZXURPWZYXVNLKIGFGGHIKLQSWX[\\[[[ZTPPOOORVWVUUVWVWXZ\\\\ZXZXYXXXVVTTSSTSRQQRRSUWXXUU\\\\[ZZYXYYXXUVX[[\\\\\\\\[\\][]]\\_gfffeccaa]ZYYUZgjihjhhhgghhgjhgihghhjhgge]bjjijihiigiigggijihiigjigibcjiiijhjhfihggakfdd_\\ZUSRPPP`hfhgehfdfedf^fihegfgfeefebeWZecacb_a`\\`^Z_\\X\\ZWYXSWSPRGFCAAAAAAAAA",
        "adddate": "2022-08-01 19:58:50",
        "free_block": "1",
        "creation": "1",
        "official": "1",
        "legal": "1",
        "duration": 370,
        "xtrack": 0,
        "xmix": 0,
        "type": "track",
        "sizebyte": 14813517,
        "srv": "4",
        "styleparts": "52,61",
        "quantityLike": 3,
        "quantityListen": 75,
        "quantityComment": 0,
        "quantityDownload": 2,
        "quantityPlaylist": 0,
        "quantityShares": 0,
        "urlname": "",
        "hash_high": "",
        "typeDownload": "PREMIUM",
        "name": "Label Worx",
        "status": "label",
        "file": "https:\/\/n1.mixupload.com\/media\/track_api\/6706\/910\/ltrack.mp3",
        "file_320": "",
        "cover": "https:\/\/static.mixupload.com\/n1\/media\/track\/6706\/910\/cover.jpg?184",
        "cover_max": "https:\/\/static.mixupload.com\/n1\/media\/track\/6706\/910\/cover-max.jpg?184",
        "avatarUser": "https:\/\/static.mixupload.com\/n0\/media\/userphoto\/2020-04-07\/5e8c5d7d0b92c-original.jpg?728",
        "lastComment": [],
        "userDisliked": false,
        "userLiked": false,
        "userPlaylist": false,
        "userListened": false,
        "file_types": {
            "mp3low": "Mp3 128",
            "mp3": "Mp3 320",
            "flac": "44100hz FLAC",
            "wav": "44100hz WAV"
        },
        "file_format": "FLAC",
        "label_urlname": "universe7",
        "label_name": "Universe7",
        "artists": [
            {
                "urlname": "andy-jornee",
                "name": "Andy Jornee"
            },
            {
                "urlname": "victoriya",
                "name": "Victoriya"
            }
        ]
    }
}
"""
