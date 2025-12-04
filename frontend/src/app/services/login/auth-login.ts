import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { IResponse } from '../../interfaces/response';
import { IToken } from '../../interfaces/token';


@Injectable({ providedIn: 'root' })
export class AuthLoginService {
  private httpClient = inject(HttpClient)

  authLoginPost(login: string, senha: string): Observable<IResponse<IToken>> {
    return this.httpClient.post<IResponse<IToken>>(
      'http://127.0.0.1:8000/api/v1/auth/login',
      { login, senha }
    );
  }
}