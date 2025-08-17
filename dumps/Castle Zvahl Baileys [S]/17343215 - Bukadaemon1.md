# 17343215 - Bukadaemon1

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Castle Zvahl Baileys [S] (ID: 138) |
| Block Size       | 320 bytes                          |
| Total Events     | 13                                 |
| References Count | 27                                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |      1 |              1 |
| [2](#event-2)            | 0x0002       |      1 |              1 |
| [14](#event-14)          | 0x0003       |      1 |              1 |
| [3](#event-3)            | 0x0004       |      1 |              1 |
| [65535.1](#event-655351) | 0x0005       |     33 |              7 |
| [65535.2](#event-655352) | 0x0026       |     14 |              4 |
| [65535.3](#event-655353) | 0x0034       |     14 |              4 |
| [65535.4](#event-655354) | 0x0042       |     14 |              4 |
| [65535.5](#event-655355) | 0x0050       |     27 |              7 |
| [65535.6](#event-655356) | 0x006B       |     17 |              5 |
| [65535.7](#event-655357) | 0x007C       |     10 |              2 |
| [65535.8](#event-655358) | 0x0086       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0012      |          18 |
|       1 | 0xFFFFFF94  |  4294967188 |
|       2 | 0x0001      |           1 |
|       3 | 0xFFFFD8F0  |  4294957296 |
|       4 | 0x001E      |          30 |
|       5 | 0x0ABC      |        2748 |
|       6 | 0x002D      |          45 |
|       7 | 0x172B      |        5931 |
|       8 | 0x194C      |        6476 |
|       9 | 0xFFF9E1F2  |  4294566386 |
|      10 | 0x4E98      |       20120 |
|      11 | 0xFFFF5802  |  4294924290 |
|      12 | 0x0028      |          40 |
|      13 | 0xFFFBC41F  |  4294689823 |
|      14 | 0x4021      |       16417 |
|      15 | 0xFFFFB515  |  4294948117 |
|      16 | 0x003C      |          60 |
|      17 | 0x0000      |           0 |
|      18 | 0x0032      |          50 |
|      19 | 0x1940F     |      103439 |
|      20 | 0x4FA0      |       20384 |
|      21 | 0xFFFFA240  |  4294943296 |
|      22 | 0x0044      |          68 |
|      23 | 0x2135D     |      136029 |
|      24 | 0x46C1      |       18113 |
|      25 | 0xFFFFA228  |  4294943272 |
|      26 | 0x0080      |         128 |

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

### Event 1

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

### Event 2

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

### Event 14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             00                                        .           
```

#### Opcodes

```
  0: 0x0004 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0005   |
| Data Size    | 33 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                32 00 80  1F 00 01 80 02 80 03 80       2..........
0010: 1F 01 6F 1C 04 80 5B 05  80 EF A2 08 01 EF A2 08  ..o...[.........
0020: 01 6B 79 6F 30 00                                 .kyo0.          
```

#### Opcodes

```
  0: 0x0005 [0x32] ExtData[1]->MainSpeed = 18* * 0.1
  1: 0x0008 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.108*, Z=0.001*, Y=-10.000*
  2: 0x0010 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0012 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0013 [0x1C] WAIT(30* ticks)
  5: 0x0016 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kyo0" with entities [Bukadaemon1 (ID: 17343215/0x0108A2EF), Bukadaemon1 (ID: 17343215/0x0108A2EF)], work=2748*
  6: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   32 06  80 1F 00 07 80 08 80 03        2.........
0030: 80 1F 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0026 [0x32] ExtData[1]->MainSpeed = 45* * 0.1
  1: 0x0029 [0x1F] MOVE_ENTITY: EventEntity moves to X=5.931*, Z=6.476*, Y=-10.000*
  2: 0x0031 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0033 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             32 04 80 1F  00 09 80 0A 80 0B 80 1F      2...........
0040: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0034 [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  1: 0x0037 [0x1F] MOVE_ENTITY: EventEntity moves to X=-400.910*, Z=20.120*, Y=-43.006*
  2: 0x003F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0041 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       32 0C 80 1F 00 0D  80 0E 80 0F 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0042 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0045 [0x1F] MOVE_ENTITY: EventEntity moves to X=-277.473*, Z=16.417*, Y=-19.179*
  2: 0x004D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 27 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 1C 10 80 4B EF A2 08 01  11 80 1C 10 80 32 12 80  ...K.........2..
0060: 1F 00 13 80 14 80 15 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x0050 [0x1C] WAIT(60* ticks)
  1: 0x0053 [0x4B] UPDATE_ENTITY_YAW(entity=Bukadaemon1 (ID: 17343215/0x0108A2EF), yaw=0.0°*)
  2: 0x005A [0x1C] WAIT(60* ticks)
  3: 0x005D [0x32] ExtData[1]->MainSpeed = 50* * 0.1
  4: 0x0060 [0x1F] MOVE_ENTITY: EventEntity moves to X=103.439*, Z=20.384*, Y=-24.000*
  5: 0x0068 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   1C 04 80 32 16             ...2.
0070: 80 1F 00 17 80 18 80 19  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x006B [0x1C] WAIT(30* ticks)
  1: 0x006E [0x32] ExtData[1]->MainSpeed = 68* * 0.1
  2: 0x0071 [0x1F] MOVE_ENTITY: EventEntity moves to X=136.029*, Z=18.113*, Y=-24.024*
  3: 0x0079 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      6C EF A2 08              l...
0080: 01 11 80 02 80 00                                 ......          
```

#### Opcodes

```
  0: 0x007C [0x6C] FADE_ENTITY_COLOR(entity_id=Bukadaemon1 (ID: 17343215/0x0108A2EF), end_alpha=0*, fade_time=1*)
  1: 0x0085 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0086   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   6C EF  A2 08 01 1A 80 02 80 00        l.........
```

#### Opcodes

```
  0: 0x0086 [0x6C] FADE_ENTITY_COLOR(entity_id=Bukadaemon1 (ID: 17343215/0x0108A2EF), end_alpha=128*, fade_time=1*)
  1: 0x008F [0x00] END_REQSTACK()
```
