import { Component, OnInit } from '@angular/core';
import { MovieService } from '../movie.service';
import { SharedService } from '../shared.service';

@Component({
  selector: 'app-movie-list',
  templateUrl: './movie-list.component.html',
  styleUrls: ['./movie-list.component.css']
})
export class MovieListComponent implements OnInit {
  movies: any[] = []; 

  constructor(private movieService: MovieService, private sharedService: SharedService) { }

  ngOnInit(): void {
    this.sharedService.selectedGenreSlug$.subscribe(selectedGenreSlug => {
      if (selectedGenreSlug) {
        this.movieService.getMoviesByGenre(selectedGenreSlug).subscribe(movies => {
          this.movies = movies;
        });
      }
    });
  }
}
