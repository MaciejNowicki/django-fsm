# -*- coding: utf-8 -*-
from async_signals import AsyncSignal

pre_transition = AsyncSignal(providing_args=['instance', 'name', 'source', 'target'])
post_transition = AsyncSignal(providing_args=['instance', 'name', 'source', 'target', 'exception'])
