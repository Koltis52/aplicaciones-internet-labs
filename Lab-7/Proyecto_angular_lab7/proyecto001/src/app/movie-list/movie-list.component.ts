import { Component, OnInit } from '@angular/core';
import { MovieService } from '../movie.service';

@Component({
  selector: 'app-movie-list',
  templateUrl: './movie-list.component.html',
  styleUrls: ['./movie-list.component.css']
})
export class MovieListComponent implements OnInit {
  movies: any[] = []; // Adjust the type based on your actual JSON structure

  constructor(private movieService: MovieService) { }

  ngOnInit(): void {
    // Fetch movie data and handle it here
    // For example, let's assume you want to display movies for the "Action" genre initially
    this.movieService.getMoviesByGenre('action').subscribe(movies => {
      this.movies = movies;
    });
  }
}
