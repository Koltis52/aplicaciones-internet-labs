import { Component, OnInit } from '@angular/core';
import { MovieService } from '../movie.service';
import { SharedService } from '../shared.service';

@Component({
  selector: 'app-genre-selector',
  templateUrl: './genre-selector.component.html',
  styleUrls: ['./genre-selector.component.css']
})
export class GenreSelectorComponent implements OnInit {
  genres: any[] = [];

  constructor(private movieService: MovieService, private sharedService: SharedService) { }

  ngOnInit(): void {
    this.movieService.getGenres().subscribe(genres => {
      this.genres = genres;
    });
  }

  onGenreSelected(event: Event): void {
    const selectedGenreSlug = (event.target as HTMLSelectElement)?.value;
    if (selectedGenreSlug) {
      this.sharedService.updateSelectedGenre(selectedGenreSlug);
    }
  }
}
