import { Routes } from '@angular/router';
import { Login } from './components/login/login';
import { Produto } from './components/produto/produto';
import { RouteGuard } from './route_guard/route_guard';


export const routes: Routes = [
    { 
        path: "", component: Login
    },
    { 
        path: "login", component: Login 
    },
    { 
        path: "produto", component: Produto, canActivate: [RouteGuard] 
    },
];
