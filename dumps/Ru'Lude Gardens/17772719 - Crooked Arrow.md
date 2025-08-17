# 17772719 - Crooked Arrow

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 248 bytes                 |
| Total Events     | 8                         |
| References Count | 19                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10048](#event-10048)    | 0x0001       |     13 |              3 |
| [65535.1](#event-655351) | 0x000E       |     10 |              2 |
| [65535.2](#event-655352) | 0x0018       |     32 |              9 |
| [10051](#event-10051)    | 0x0038       |     13 |              3 |
| [122](#event-122)        | 0x0045       |      1 |              1 |
| [65535.3](#event-655353) | 0x0046       |     10 |              2 |
| [65535.4](#event-655354) | 0x0050       |     43 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0384      |         900 |
|       1 | 0x7BF8      |       31736 |
|       2 | 0x07CF      |        1999 |
|       3 | 0x0C3A      |        3130 |
|       4 | 0x0028      |          40 |
|       5 | 0x9F2E      |       40750 |
|       6 | 0x0762      |        1890 |
|       7 | 0xAEEF      |       44783 |
|       8 | 0x090C      |        2316 |
|       9 | 0x0026      |          38 |
|      10 | 0x0797      |        1943 |
|      11 | 0x999F      |       39327 |
|      12 | 0x04B4      |        1204 |
|      13 | 0x85B9      |       34233 |
|      14 | 0x0478      |        1144 |
|      15 | 0x474C      |       18252 |
|      16 | 0x0BB7      |        2999 |
|      17 | 0x0000      |           0 |
|      18 | 0x0001      |           1 |

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

### Event 10048

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 94  01 F8 FF FF 7F 00         .............  
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            37 00                7.
0010: 80 01 80 02 80 03 80 00                           ........        
```

#### Opcodes

```
  0: 0x000E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.900*, z=31.736*, y=1.999*, direction=275.1°*
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 32 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          32 04 80 1F 00 00 80 05          2.......
0020: 80 02 80 1F 01 6F 1E 07  30 0F 01 79 00 AF 30 0F  .....o..0..y..0.
0030: 01 F0 FF FF 7F 6F 70 00                           .....op.        
```

#### Opcodes

```
  0: 0x0018 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=0.900*, Z=40.750*, Y=1.999*
  2: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0025 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0026 [0x1E] EventEntity looks at Wolfgang (ID: 17772551/0x010F3007) and starts talking
  5: 0x002B [0x79] Crooked Arrow (ID: 17772719/0x010F30AF) looks at LocalPlayer (Basic look)
  6: 0x0035 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0036 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  8: 0x0037 [0x00] END_REQSTACK()
```

### Event 10051

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          92 01 F8 FF FF 7F 94 01          ........
0040: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x0038 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x003E [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0044 [0x00] END_REQSTACK()
```

### Event 122

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                00                                      .          
```

#### Opcodes

```
  0: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   37 06  80 07 80 02 80 08 80 00        7.........
```

#### Opcodes

```
  0: 0x0046 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=1.890*, z=44.783*, y=1.999*, direction=203.5°*
  1: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 43 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 32 09 80 1F 00 0A 80 0B  80 02 80 1F 01 1F 00 0C  2...............
0060: 80 0D 80 02 80 1F 01 1F  00 0E 80 0F 80 10 80 1F  ................
0070: 01 6C F8 FF FF 7F 11 80  12 80 00                 .l.........     
```

#### Opcodes

```
  0: 0x0050 [0x32] ExtData[1]->MainSpeed = 38* * 0.1
  1: 0x0053 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.943*, Z=39.327*, Y=1.999*
  2: 0x005B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005D [0x1F] MOVE_ENTITY: EventEntity moves to X=1.204*, Z=34.233*, Y=1.999*
  4: 0x0065 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0067 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.144*, Z=18.252*, Y=2.999*
  6: 0x006F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0071 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  8: 0x007A [0x00] END_REQSTACK()
```
