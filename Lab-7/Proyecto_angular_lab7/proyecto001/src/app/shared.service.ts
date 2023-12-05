import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  private selectedGenreSource = new BehaviorSubject<string>('');
  selectedGenreSlug$ = this.selectedGenreSource.asObservable();

  updateSelectedGenre(slug: string): void {
    this.selectedGenreSource.next(slug);
  }
}
