# 17339061 - Oliverain

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Xarcabard [S] (ID: 137) |
| Block Size       | 360 bytes               |
| Total Events     | 15                      |
| References Count | 21                      |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0002       |     18 |              4 |
| [65535.3](#event-655353)   | 0x0014       |     10 |              2 |
| [65535.4](#event-655354)   | 0x001E       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0027       |      9 |              3 |
| [65535.6](#event-655356)   | 0x0030       |     10 |              2 |
| [65535.7](#event-655357)   | 0x003A       |     10 |              2 |
| [4](#event-4)              | 0x0044       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0045       |     21 |              5 |
| [65535.9](#event-655359)   | 0x005A       |     21 |              2 |
| [65535.10](#event-6553510) | 0x006F       |     21 |              2 |
| [6](#event-6)              | 0x0084       |      1 |              1 |
| [65535.11](#event-6553511) | 0x0085       |     34 |              4 |
| [65535.12](#event-6553512) | 0x00A7       |     30 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x74136     |      475446 |
|       4 | 0xFFFCF08A  |  4294766730 |
|       5 | 0x4E1F      |       19999 |
|       6 | 0x0003      |           3 |
|       7 | 0x000A      |          10 |
|       8 | 0x0038      |          56 |
|       9 | 0x000C      |          12 |
|      10 | 0x010E      |         270 |
|      11 | 0x001B      |          27 |
|      12 | 0x0002      |           2 |
|      13 | 0x00D2      |         210 |
|      14 | 0x001D      |          29 |
|      15 | 0x0046      |          70 |
|      16 | 0x0063      |          99 |
|      17 | 0x71BD1     |      465873 |
|      18 | 0xFFFCE9A0  |  4294764960 |
|      19 | 0x51B1      |       20913 |
|      20 | 0x0018      |          24 |

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 2F 00 F8 FF  FF 7F 6C F8 FF FF 7F 00    "./.....l.....
0010: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             6C F8 FF FF  7F 02 80 01 80 00            l.........  
```

#### Opcodes

```
  0: 0x0014 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            22 00                ".
0020: 2F 00 F8 FF FF 7F 00                              /......         
```

#### Opcodes

```
  0: 0x001E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0020 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      22  01 2F 01 F8 FF FF 7F 00         "./......
```

#### Opcodes

```
  0: 0x0027 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0029 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 6C F8 FF FF 7F 00 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0030 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                6C F8 FF FF 7F 02            l.....
0040: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x003A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             00                                        .           
```

#### Opcodes

```
  0: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                1F 00 03  80 04 80 05 80 1F 01 6F       ..........o
0050: 4A B5 92 08 01 D7 92 08  01 00                    J.........      
```

#### Opcodes

```
  0: 0x0045 [0x1F] MOVE_ENTITY: EventEntity moves to X=475.446*, Z=-200.566*, Y=19.999*
  1: 0x004D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x004F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0050 [0x4A] Oliverain (ID: 17339061/0x010892B5) looks at Phillieulais (ID: 17339095/0x010892D7)
  4: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                B6 0B 06 80 07 80            ......
0060: 08 80 09 80 09 80 09 80  09 80 0A 80 0B 80 00     ............... 
```

#### Opcodes

```
  0: 0x005A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=10*, head=56*, body=12*, hands=12*, legs=12*, feet=12*, main=270*, sub=27*)
  1: 0x006E [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006F   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               B6                 .
0070: 0B 06 80 0C 80 09 80 09  80 09 80 09 80 09 80 0D  ................
0080: 80 00 80 00                                       ....            
```

#### Opcodes

```
  0: 0x006F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=2*, head=12*, body=12*, hands=12*, legs=12*, feet=12*, main=210*, sub=0*)
  1: 0x0083 [0x00] END_REQSTACK()
```

### Event 6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0084  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             00                                        .           
```

#### Opcodes

```
  0: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0085   |
| Data Size    | 34 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                66 0E 80  B5 92 08 01 B5 92 08 01       f..........
0090: 73 68 61 31 1C 0F 80 66  10 80 B5 92 08 01 B5 92  sha1...f........
00A0: 08 01 73 70 61 30 00                              ..spa0.         
```

#### Opcodes

```
  0: 0x0085 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [Oliverain (ID: 17339061/0x010892B5), Oliverain (ID: 17339061/0x010892B5)], work=29*
  1: 0x0094 [0x1C] WAIT(70* ticks)
  2: 0x0097 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "spa0" with entities [Oliverain (ID: 17339061/0x010892B5), Oliverain (ID: 17339061/0x010892B5)], work=99*
  3: 0x00A6 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 30 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      1F  00 11 80 12 80 13 80 1F         .........
00B0: 01 6F 1C 07 80 66 14 80  B5 92 08 01 B5 92 08 01  .o...f..........
00C0: 31 72 64 79 00                                    1rdy.           
```

#### Opcodes

```
  0: 0x00A7 [0x1F] MOVE_ENTITY: EventEntity moves to X=465.873*, Z=-202.336*, Y=20.913*
  1: 0x00AF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x00B1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00B2 [0x1C] WAIT(10* ticks)
  4: 0x00B5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rdy" with entities [Oliverain (ID: 17339061/0x010892B5), Oliverain (ID: 17339061/0x010892B5)], work=24*
  5: 0x00C4 [0x00] END_REQSTACK()
```
