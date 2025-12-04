import { Component, inject } from '@angular/core';
import { FormGroup, FormControl, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { AuthLoginService } from '../../services/login/auth-login';
import { Router } from '@angular/router';


@Component({
  selector: 'app-login',
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './login.html',
  styleUrl: './login.css',
})
export class Login {
  httpClient = inject(AuthLoginService);
  router: Router = inject(Router);
  loginFormGroup = new FormGroup({
    login: new FormControl('', Validators.required),
    senha: new FormControl('', Validators.required),
  });
  
  onSubmit() {
    if (this.loginFormGroup.valid) {

      this.httpClient.authLoginPost(this.loginFormGroup.value.login!, this.loginFormGroup.value.senha!).subscribe(
        (response) => { 
          localStorage.setItem('access_token', response.body.access_token);
          localStorage.setItem('refresh_token', response.body.refresh_token);
          this.router.navigate(['/produto']);
        }
      );
    }

  }
}
