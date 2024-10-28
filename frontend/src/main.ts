import { AppModule } from './app.module';
import { AppComponent } from './components/app/app.component';
import { bootstrapApplication } from '@angular/platform-browser';
import { importProvidersFrom } from '@angular/core';

bootstrapApplication(AppComponent, {
  providers: [
    importProvidersFrom(AppModule)
  ]
}).catch(err => console.error(err));
