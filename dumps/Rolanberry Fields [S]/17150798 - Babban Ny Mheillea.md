# 17150798 - Babban Ny Mheillea

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Rolanberry Fields [S] (ID: 91) |
| Block Size       | 504 bytes                      |
| Total Events     | 15                             |
| References Count | 19                             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [5](#event-5)              | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     44 |              4 |
| [65535.2](#event-655352)   | 0x002E       |     16 |              5 |
| [65535.3](#event-655353)   | 0x003E       |     29 |              3 |
| [65535.4](#event-655354)   | 0x005B       |     29 |              3 |
| [65535.5](#event-655355)   | 0x0078       |     29 |              3 |
| [65535.6](#event-655356)   | 0x0095       |     29 |              3 |
| [65535.7](#event-655357)   | 0x00B2       |     30 |              8 |
| [65535.8](#event-655358)   | 0x00D0       |     14 |              4 |
| [65535.9](#event-655359)   | 0x00DE       |     57 |              5 |
| [65535.10](#event-6553510) | 0x0117       |     14 |              4 |
| [65535.11](#event-6553511) | 0x0125       |     16 |              4 |
| [65535.12](#event-6553512) | 0x0135       |     29 |              3 |
| [65535.13](#event-6553513) | 0x0152       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0871      |        2161 |
|       1 | 0x086E      |        2158 |
|       2 | 0x0011      |          17 |
|       3 | 0xFFFEE985  |  4294896005 |
|       4 | 0xFFF26CC4  |  4294077636 |
|       5 | 0xFFFFFECE  |  4294966990 |
|       6 | 0x0384      |         900 |
|       7 | 0x000F      |          15 |
|       8 | 0x01F4      |         500 |
|       9 | 0x04B0      |        1200 |
|      10 | 0xFFFEE81E  |  4294895646 |
|      11 | 0xFFF27944  |  4294080836 |
|      12 | 0x0070      |         112 |
|      13 | 0x02DA      |         730 |
|      14 | 0x0190      |         400 |
|      15 | 0x000A      |          10 |
|      16 | 0x1FB66     |      129894 |
|      17 | 0xFFF9C69F  |  4294559391 |
|      18 | 0x5ED4      |       24276 |

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

### Event 5

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 44 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       5B 00 80 4E B3 05  01 4E B3 05 01 73 61 69    [..N...N...sai
0010: 31 5B 01 80 4F B3 05 01  4F B3 05 01 73 61 69 31  1[..O...O...sai1
0020: 53 4F B3 05 01 4F B3 05  01 73 61 69 31 00        SO...O...sai1.  
```

#### Opcodes

```
  0: 0x0002 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sai1" with entities [Babban Ny Mheillea (ID: 17150798/0x0105B34E), Babban Ny Mheillea (ID: 17150798/0x0105B34E)], work=2161*
  1: 0x0011 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sai1" with entities [Abenzio (ID: 17150799/0x0105B34F), Abenzio (ID: 17150799/0x0105B34F)], work=2158*
  2: 0x0020 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sai1" with entities [Abenzio (ID: 17150799/0x0105B34F), Abenzio (ID: 17150799/0x0105B34F)]
  3: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            33 00                3.
0030: 32 02 80 1F 00 03 80 04  80 05 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x002E [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  1: 0x0030 [0x32] ExtData[1]->MainSpeed = 17* * 0.1
  2: 0x0033 [0x1F] MOVE_ENTITY: EventEntity moves to X=-71.291*, Z=-889.660*, Y=-0.306*
  3: 0x003B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            5B 00                [.
0040: 80 4E B3 05 01 4E B3 05  01 77 68 74 30 53 4E B3  .N...N...wht0SN.
0050: 05 01 4E B3 05 01 77 68  74 30 00                 ..N...wht0.     
```

#### Opcodes

```
  0: 0x003E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wht0" with entities [Babban Ny Mheillea (ID: 17150798/0x0105B34E), Babban Ny Mheillea (ID: 17150798/0x0105B34E)], work=2161*
  1: 0x004D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "wht0" with entities [Babban Ny Mheillea (ID: 17150798/0x0105B34E), Babban Ny Mheillea (ID: 17150798/0x0105B34E)]
  2: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   5B 00 80 4E B3             [..N.
0060: 05 01 4E B3 05 01 77 68  74 31 53 4E B3 05 01 4E  ..N...wht1SN...N
0070: B3 05 01 77 68 74 30 00                           ...wht0.        
```

#### Opcodes

```
  0: 0x005B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wht1" with entities [Babban Ny Mheillea (ID: 17150798/0x0105B34E), Babban Ny Mheillea (ID: 17150798/0x0105B34E)], work=2161*
  1: 0x006A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "wht0" with entities [Babban Ny Mheillea (ID: 17150798/0x0105B34E), Babban Ny Mheillea (ID: 17150798/0x0105B34E)]
  2: 0x0077 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          5B 00 80 4E B3 05 01 4E          [..N...N
0080: B3 05 01 74 6C 6B 30 53  4E B3 05 01 4E B3 05 01  ...tlk0SN...N...
0090: 74 6C 6B 30 00                                    tlk0.           
```

#### Opcodes

```
  0: 0x0078 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Babban Ny Mheillea (ID: 17150798/0x0105B34E), Babban Ny Mheillea (ID: 17150798/0x0105B34E)], work=2161*
  1: 0x0087 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [Babban Ny Mheillea (ID: 17150798/0x0105B34E), Babban Ny Mheillea (ID: 17150798/0x0105B34E)]
  2: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                5B 00 80  4E B3 05 01 4E B3 05 01       [..N...N...
00A0: 74 6C 6B 31 53 4E B3 05  01 4E B3 05 01 74 6C 6B  tlk1SN...N...tlk
00B0: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x0095 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Babban Ny Mheillea (ID: 17150798/0x0105B34E), Babban Ny Mheillea (ID: 17150798/0x0105B34E)], work=2161*
  1: 0x00A4 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [Babban Ny Mheillea (ID: 17150798/0x0105B34E), Babban Ny Mheillea (ID: 17150798/0x0105B34E)]
  2: 0x00B1 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B2   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       4B F8 FF FF 7F 06  80 6F 76 F8 FF FF 7F 1C    K......ov.....
00C0: 07 80 4B F8 FF FF 7F 08  80 6F 76 F8 FF FF 7F 00  ..K......ov.....
```

#### Opcodes

```
  0: 0x00B2 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=4.9°*)
  1: 0x00B9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00BA [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  3: 0x00BF [0x1C] WAIT(15* ticks)
  4: 0x00C2 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=2.7°*)
  5: 0x00C9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x00CA [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  7: 0x00CF [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D0   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0: 4B F8 FF FF 7F 09 80 6F  76 F8 FF FF 7F 00        K......ov.....  
```

#### Opcodes

```
  0: 0x00D0 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=6.6°*)
  1: 0x00D7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00D8 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  3: 0x00DD [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DE   |
| Data Size    | 57 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                            BA 4E                .N
00E0: B3 05 01 0A 80 0B 80 0C  80 0D 80 5B 01 80 4F B3  ...........[..O.
00F0: 05 01 4F B3 05 01 73 61  69 30 5B 00 80 4E B3 05  ..O...sai0[..N..
0100: 01 4E B3 05 01 73 61 69  30 53 4E B3 05 01 4E B3  .N...sai0SN...N.
0110: 05 01 73 61 69 30 00                              ..sai0.         
```

#### Opcodes

```
  0: 0x00DE [0xBA] SET_ENTITY_POSITION(entity_id=Babban Ny Mheillea (ID: 17150798/0x0105B34E), pos_x=-71.650*, pos_z=-886.460*, pos_y=0.112*, direction=64.2°*)
  1: 0x00EB [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sai0" with entities [Abenzio (ID: 17150799/0x0105B34F), Abenzio (ID: 17150799/0x0105B34F)], work=2158*
  2: 0x00FA [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sai0" with entities [Babban Ny Mheillea (ID: 17150798/0x0105B34E), Babban Ny Mheillea (ID: 17150798/0x0105B34E)], work=2161*
  3: 0x0109 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sai0" with entities [Babban Ny Mheillea (ID: 17150798/0x0105B34E), Babban Ny Mheillea (ID: 17150798/0x0105B34E)]
  4: 0x0116 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0117   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                      4B  F8 FF FF 7F 0E 80 6F 76         K......ov
0120: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0117 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=2.2°*)
  1: 0x011E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x011F [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  3: 0x0124 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0125   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                4A F8 FF  FF 7F 51 B3 05 01 6F 76       J....Q...ov
0130: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0125 [0x4A] EventEntity looks at Camlin (ID: 17150801/0x0105B351)
  1: 0x012E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x012F [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  3: 0x0134 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0135   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                5B 00 80  4E B3 05 01 4E B3 05 01       [..N...N...
0140: 62 69 6B 30 53 4E B3 05  01 4E B3 05 01 62 69 6B  bik0SN...N...bik
0150: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0135 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bik0" with entities [Babban Ny Mheillea (ID: 17150798/0x0105B34E), Babban Ny Mheillea (ID: 17150798/0x0105B34E)], work=2161*
  1: 0x0144 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bik0" with entities [Babban Ny Mheillea (ID: 17150798/0x0105B34E), Babban Ny Mheillea (ID: 17150798/0x0105B34E)]
  2: 0x0151 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0152   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:       32 0F 80 1F 00 10  80 11 80 12 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0152 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x0155 [0x1F] MOVE_ENTITY: EventEntity moves to X=129.894*, Z=-407.905*, Y=24.276*
  2: 0x015D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x015F [0x00] END_REQSTACK()
```
