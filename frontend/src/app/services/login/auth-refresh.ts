import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { IResponse } from '../../interfaces/response';
import { IToken } from '../../interfaces/token';
import { enviromont } from '../../../environments/environment';


@Injectable({ providedIn: 'root' })
export class AuthRefreshService {
  private httpClient = inject(HttpClient)

  authRefreshGet(): Observable<IResponse<IToken>> {
    return this.httpClient.get<IResponse<IToken>>(
      `${enviromont.baseUrl}/auth/refresh`
    );
  }
}
