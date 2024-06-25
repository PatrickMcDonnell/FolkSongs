const audioPlayer = document.getElementById('audioPlayer');
const audioSource = document.getElementById('audioSource');
const songList = document.getElementById('songList');

const songs = [
    { title: "Song 1", url: "https://example.com/song1.mp3" },
    { title: "Song 2", url: "https://example.com/song2.mp3" },
    // Add more songs here
];

songs.forEach((song, index) => {
    const li = document.createElement('li');
    li.textContent = song.title;
    li.addEventListener('click', () => {
        audioSource.src = song.url;
        audioPlayer.load();
        audioPlayer.play();
    });
    songList.appendChild(li);
});
