import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { provideHttpClient, withInterceptorsFromDi  } from '@angular/common/http';
import { PostListComponent } from './components/post-list/post-list.component';
import { PostService } from './services/post.service';
import { UserListComponent } from './components/user-list/user-list.component';
import { UserService } from './services/user.service';
import { AppRoutingModule } from './app.routing-module';

@NgModule({
  declarations: [
    PostListComponent,
    UserListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [PostService, UserService, provideHttpClient(withInterceptorsFromDi())],
})
export class AppModule { }
