import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

interface Genre {
  id: string;
  vendorka_id: string;
  name: string;
  slug: string;
  position: string;
  content_count: string;
  updated_at: string;
  description: string | null;
  images: { url: string; width: number; height: number; type: string }[];
}

interface Movie {
  _id: string;
  genres: string[];
  keywords: string[];
}

@Injectable({
  providedIn: 'root'
})
export class MovieService {
  private apiUrl = 'http://api.filmon.com/api/vod';

  constructor(private http: HttpClient) { }

  getGenres(): Observable<Genre[]> {
    return this.http.get<{ response: Genre[] }>(`${this.apiUrl}/genres`).pipe(
      map(response => response.response)
    );
  }

  getMoviesByGenre(genre: string): Observable<Movie[]> {
    return this.http.get<{ response: Movie[] }>(`${this.apiUrl}/search?genre=${genre}`).pipe(
      map(response => response.response)
    );
  }
}
