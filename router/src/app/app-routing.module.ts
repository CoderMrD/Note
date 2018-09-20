import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ProductComponent } from './product/product.component';
import { Code404Component } from './code404/code404.component';
import { ProductDescComponent } from './product-desc/product-desc.component';
import { SellerInfoComponent } from './seller-info/seller-info.component';

const routes: Routes = [
  // 配置一个空路由指向home组件,path里面不能用斜杠/开头，为了自由的使用相对路径和绝对路径
  // 访问根路由时，重定向到home
  {path: '',redirectTo: '/home',pathMatch: 'full'},
  {path: 'home',component: HomeComponent},
  {path: 'product/:id',component: ProductComponent,children:[
    {path:'',component:ProductDescComponent},
    {path:'seller/:id',component:SellerInfoComponent}
  ]},
  {path: '**',component:Code404Component}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
