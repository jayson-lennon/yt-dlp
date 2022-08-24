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

        data = self._download_json(api_url, video_id)

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
