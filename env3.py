#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Импортируем модуль os
import os
# Проверяем значение переменной среды
if os.environ.get('DEBUG') == 'True':
   print('Debug mode is on')
else:
   print('Debug mode is off')
