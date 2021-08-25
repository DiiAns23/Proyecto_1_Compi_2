import { TestBed } from '@angular/core/testing';

import { AnalizadorService } from './analizador.service';

describe('AnalizadorService', () => {
  let service: AnalizadorService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AnalizadorService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
