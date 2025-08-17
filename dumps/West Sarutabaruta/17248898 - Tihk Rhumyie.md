# 17248898 - Tihk Rhumyie

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | West Sarutabaruta (ID: 115) |
| Block Size       | 484 bytes                   |
| Total Events     | 10                          |
| References Count | 11                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      1 |              1 |
| [65535.2](#event-655352) | 0x0002       |      1 |              1 |
| [65535.3](#event-655353) | 0x0003       |    121 |             21 |
| [65535.4](#event-655354) | 0x007C       |     24 |              6 |
| [65535.5](#event-655355) | 0x0094       |    121 |             21 |
| [65535.6](#event-655356) | 0x010D       |     14 |              4 |
| [65535.7](#event-655357) | 0x011B       |     24 |              6 |
| [65535.8](#event-655358) | 0x0133       |     73 |             11 |
| [65535.9](#event-655359) | 0x017C       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000B      |          11 |
|       1 | 0x2178      |        8568 |
|       2 | 0x5524      |       21796 |
|       3 | 0xFFFFFC18  |  4294966296 |
|       4 | 0x000F      |          15 |
|       5 | 0x02AF      |         687 |
|       6 | 0x690E      |       26894 |
|       7 | 0x2CA0      |       11424 |
|       8 | 0x0000      |           0 |
|       9 | 0x0001      |           1 |
|      10 | 0x0078      |         120 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0003    |
| Data Size    | 121 bytes |
| Instructions | 21        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          2F 00 82 32 07  01 2F 00 83 32 07 01 2F     /..2../..2../
0010: 00 84 32 07 01 2F 00 86  32 07 01 2F 00 87 32 07  ..2../..2../..2.
0020: 01 4E 00 82 32 07 01 4E  00 83 32 07 01 4E 00 84  .N..2..N..2..N..
0030: 32 07 01 4E 00 86 32 07  01 4E 00 87 32 07 01 92  2..N..2..N..2...
0040: 01 82 32 07 01 92 01 83  32 07 01 92 01 84 32 07  ..2.....2.....2.
0050: 01 92 01 86 32 07 01 92  01 87 32 07 01 94 01 82  ....2.....2.....
0060: 32 07 01 94 01 83 32 07  01 94 01 84 32 07 01 94  2.....2.....2...
0070: 01 86 32 07 01 94 01 87  32 07 01 00              ..2.....2...    
```

#### Opcodes

```
  0: 0x0003 [0x2F] Tihk Rhumyie (ID: 17248898/0x01073282)->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0009 [0x2F] Kuppo-Pippo (ID: 17248899/0x01073283)->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000F [0x2F] Karanka-Tonka (ID: 17248900/0x01073284)->Render.Flags0 &= ~0x80000 // Bit 19
  3: 0x0015 [0x2F] Cotta-Lotta (ID: 17248902/0x01073286)->Render.Flags0 &= ~0x80000 // Bit 19
  4: 0x001B [0x2F] Tacca-Picca (ID: 17248903/0x01073287)->Render.Flags0 &= ~0x80000 // Bit 19
  5: 0x0021 [0x4E] SET_ENTITY_HIDE_FLAG: Show Tihk Rhumyie (ID: 17248898/0x01073282)
  6: 0x0027 [0x4E] SET_ENTITY_HIDE_FLAG: Show Kuppo-Pippo (ID: 17248899/0x01073283)
  7: 0x002D [0x4E] SET_ENTITY_HIDE_FLAG: Show Karanka-Tonka (ID: 17248900/0x01073284)
  8: 0x0033 [0x4E] SET_ENTITY_HIDE_FLAG: Show Cotta-Lotta (ID: 17248902/0x01073286)
  9: 0x0039 [0x4E] SET_ENTITY_HIDE_FLAG: Show Tacca-Picca (ID: 17248903/0x01073287)
 10: 0x003F [0x92] Tihk Rhumyie (ID: 17248898/0x01073282)->Render.Flags3 ^= 0x01
 11: 0x0045 [0x92] Kuppo-Pippo (ID: 17248899/0x01073283)->Render.Flags3 ^= 0x01
 12: 0x004B [0x92] Karanka-Tonka (ID: 17248900/0x01073284)->Render.Flags3 ^= 0x01
 13: 0x0051 [0x92] Cotta-Lotta (ID: 17248902/0x01073286)->Render.Flags3 ^= 0x01
 14: 0x0057 [0x92] Tacca-Picca (ID: 17248903/0x01073287)->Render.Flags3 ^= 0x01
 15: 0x005D [0x94] Tihk Rhumyie (ID: 17248898/0x01073282)->Render.Flags3 ^= 0x01
 16: 0x0063 [0x94] Kuppo-Pippo (ID: 17248899/0x01073283)->Render.Flags3 ^= 0x01
 17: 0x0069 [0x94] Karanka-Tonka (ID: 17248900/0x01073284)->Render.Flags3 ^= 0x01
 18: 0x006F [0x94] Cotta-Lotta (ID: 17248902/0x01073286)->Render.Flags3 ^= 0x01
 19: 0x0075 [0x94] Tacca-Picca (ID: 17248903/0x01073287)->Render.Flags3 ^= 0x01
 20: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      32 00 80 1F              2...
0080: 00 01 80 02 80 03 80 1F  01 6F 4A 82 32 07 01 81  .........oJ.2...
0090: 32 07 01 00                                       2...            
```

#### Opcodes

```
  0: 0x007C [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x007F [0x1F] MOVE_ENTITY: EventEntity moves to X=8.568*, Z=21.796*, Y=-1.000*
  2: 0x0087 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0089 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x008A [0x4A] Tihk Rhumyie (ID: 17248898/0x01073282) looks at Khoto Rokkorah (ID: 17248897/0x01073281)
  5: 0x0093 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0094    |
| Data Size    | 121 bytes |
| Instructions | 21        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             2F 00 88 32  07 01 2F 00 87 32 07 01      /..2../..2..
00A0: 2F 00 86 32 07 01 2F 00  85 32 07 01 2F 00 83 32  /..2../..2../..2
00B0: 07 01 4E 00 88 32 07 01  4E 00 87 32 07 01 4E 00  ..N..2..N..2..N.
00C0: 86 32 07 01 4E 00 85 32  07 01 4E 00 83 32 07 01  .2..N..2..N..2..
00D0: 92 01 88 32 07 01 92 01  87 32 07 01 92 01 86 32  ...2.....2.....2
00E0: 07 01 92 01 85 32 07 01  92 01 83 32 07 01 94 01  .....2.....2....
00F0: 88 32 07 01 94 01 87 32  07 01 94 01 86 32 07 01  .2.....2.....2..
0100: 94 01 85 32 07 01 94 01  83 32 07 01 00           ...2.....2...   
```

#### Opcodes

```
  0: 0x0094 [0x2F] Rahmi Yamilahto (ID: 17248904/0x01073288)->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x009A [0x2F] Tacca-Picca (ID: 17248903/0x01073287)->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x00A0 [0x2F] Cotta-Lotta (ID: 17248902/0x01073286)->Render.Flags0 &= ~0x80000 // Bit 19
  3: 0x00A6 [0x2F] Noh Ramyoh (ID: 17248901/0x01073285)->Render.Flags0 &= ~0x80000 // Bit 19
  4: 0x00AC [0x2F] Kuppo-Pippo (ID: 17248899/0x01073283)->Render.Flags0 &= ~0x80000 // Bit 19
  5: 0x00B2 [0x4E] SET_ENTITY_HIDE_FLAG: Show Rahmi Yamilahto (ID: 17248904/0x01073288)
  6: 0x00B8 [0x4E] SET_ENTITY_HIDE_FLAG: Show Tacca-Picca (ID: 17248903/0x01073287)
  7: 0x00BE [0x4E] SET_ENTITY_HIDE_FLAG: Show Cotta-Lotta (ID: 17248902/0x01073286)
  8: 0x00C4 [0x4E] SET_ENTITY_HIDE_FLAG: Show Noh Ramyoh (ID: 17248901/0x01073285)
  9: 0x00CA [0x4E] SET_ENTITY_HIDE_FLAG: Show Kuppo-Pippo (ID: 17248899/0x01073283)
 10: 0x00D0 [0x92] Rahmi Yamilahto (ID: 17248904/0x01073288)->Render.Flags3 ^= 0x01
 11: 0x00D6 [0x92] Tacca-Picca (ID: 17248903/0x01073287)->Render.Flags3 ^= 0x01
 12: 0x00DC [0x92] Cotta-Lotta (ID: 17248902/0x01073286)->Render.Flags3 ^= 0x01
 13: 0x00E2 [0x92] Noh Ramyoh (ID: 17248901/0x01073285)->Render.Flags3 ^= 0x01
 14: 0x00E8 [0x92] Kuppo-Pippo (ID: 17248899/0x01073283)->Render.Flags3 ^= 0x01
 15: 0x00EE [0x94] Rahmi Yamilahto (ID: 17248904/0x01073288)->Render.Flags3 ^= 0x01
 16: 0x00F4 [0x94] Tacca-Picca (ID: 17248903/0x01073287)->Render.Flags3 ^= 0x01
 17: 0x00FA [0x94] Cotta-Lotta (ID: 17248902/0x01073286)->Render.Flags3 ^= 0x01
 18: 0x0100 [0x94] Noh Ramyoh (ID: 17248901/0x01073285)->Render.Flags3 ^= 0x01
 19: 0x0106 [0x94] Kuppo-Pippo (ID: 17248899/0x01073283)->Render.Flags3 ^= 0x01
 20: 0x010C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                         32 04 80               2..
0110: 1F 00 05 80 06 80 03 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x010D [0x32] ExtData[1]->MainSpeed = 15* * 0.1
  1: 0x0110 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.687*, Z=26.894*, Y=-1.000*
  2: 0x0118 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x011A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011B   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                   4A 82 32 07 01             J.2..
0120: 84 32 07 01 6F 76 82 32  07 01 2B 82 32 07 01 07  .2..ov.2..+.2...
0130: 80 23 00                                          .#.             
```

#### Opcodes

```
  0: 0x011B [0x4A] Tihk Rhumyie (ID: 17248898/0x01073282) looks at Karanka-Tonka (ID: 17248900/0x01073284)
  1: 0x0124 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0125 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Tihk Rhumyie (ID: 17248898/0x01073282) Render.Flags0 and Render.Flags3 conditions are met
  3: 0x012A [0x2B] Tihk Rhumyie (ID: 17248898/0x01073282) [11424*]:
    → "Wait, wait. What happens next?"
  4: 0x0131 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0132 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0133   |
| Data Size    | 73 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:          6C 82 32 07 01  08 80 09 80 6C 83 32 07     l.2......l.2.
0140: 01 08 80 09 80 6C 84 32  07 01 08 80 09 80 6C 86  .....l.2......l.
0150: 32 07 01 08 80 09 80 6C  87 32 07 01 08 80 09 80  2......l.2......
0160: 4A F0 FF FF 7F 81 32 07  01 4A 81 32 07 01 F0 FF  J.....2..J.2....
0170: FF 7F 6F 76 81 32 07 01  1C 0A 80 00              ..ov.2......    
```

#### Opcodes

```
  0: 0x0133 [0x6C] FADE_ENTITY_COLOR(entity_id=Tihk Rhumyie (ID: 17248898/0x01073282), end_alpha=0*, fade_time=1*)
  1: 0x013C [0x6C] FADE_ENTITY_COLOR(entity_id=Kuppo-Pippo (ID: 17248899/0x01073283), end_alpha=0*, fade_time=1*)
  2: 0x0145 [0x6C] FADE_ENTITY_COLOR(entity_id=Karanka-Tonka (ID: 17248900/0x01073284), end_alpha=0*, fade_time=1*)
  3: 0x014E [0x6C] FADE_ENTITY_COLOR(entity_id=Cotta-Lotta (ID: 17248902/0x01073286), end_alpha=0*, fade_time=1*)
  4: 0x0157 [0x6C] FADE_ENTITY_COLOR(entity_id=Tacca-Picca (ID: 17248903/0x01073287), end_alpha=0*, fade_time=1*)
  5: 0x0160 [0x4A] LocalPlayer looks at Khoto Rokkorah (ID: 17248897/0x01073281)
  6: 0x0169 [0x4A] Khoto Rokkorah (ID: 17248897/0x01073281) looks at LocalPlayer
  7: 0x0172 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0173 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Khoto Rokkorah (ID: 17248897/0x01073281) Render.Flags0 and Render.Flags3 conditions are met
  9: 0x0178 [0x1C] WAIT(120* ticks)
 10: 0x017B [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x017C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                      00                       .   
```

#### Opcodes

```
  0: 0x017C [0x00] END_REQSTACK()
```
