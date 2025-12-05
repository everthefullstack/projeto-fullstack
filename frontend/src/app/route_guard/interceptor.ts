import { HttpInterceptorFn } from '@angular/common/http';
import { catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';
import { inject } from '@angular/core';
import { Router } from '@angular/router';


export const Interceptor: HttpInterceptorFn = (req, next) => {
  const router = inject(Router);

  return next(req).pipe(
    catchError((error) => {
      if (error.status === 401) {
        router.navigate(['/login'], { queryParams: { msg: error.error.message } });
      } else if (error.status === 403) {
        router.navigate(['/login'], { queryParams: { msg: 'Você não tem permissão para acessar este recurso.' } });
      }
      return throwError(() => error);
    })
  );
};
