# 17056428 - Rughadjeen

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Aydeewa Subterrane (ID: 68) |
| Block Size       | 372 bytes                   |
| Total Events     | 9                           |
| References Count | 32                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [34](#event-34)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     29 |              7 |
| [65535.2](#event-655352) | 0x001F       |     20 |              6 |
| [65535.3](#event-655353) | 0x0033       |     20 |              6 |
| [65535.4](#event-655354) | 0x0047       |     49 |              9 |
| [65535.5](#event-655355) | 0x0078       |     31 |              9 |
| [65535.6](#event-655356) | 0x0097       |     20 |              6 |
| [65535.7](#event-655357) | 0x00AB       |     20 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x15508     |       87304 |
|       1 | 0x97DE      |       38878 |
|       2 | 0x01E0      |         480 |
|       3 | 0x0C8E      |        3214 |
|       4 | 0x0028      |          40 |
|       5 | 0x1424F     |       82511 |
|       6 | 0xBC8A      |       48266 |
|       7 | 0x000D      |          13 |
|       8 | 0x13CEF     |       81135 |
|       9 | 0xC14E      |       49486 |
|      10 | 0x13914     |       80148 |
|      11 | 0x7377      |       29559 |
|      12 | 0xFFFFFEC5  |  4294966981 |
|      13 | 0x13787     |       79751 |
|      14 | 0x6B56      |       27478 |
|      15 | 0xFFFFFEBC  |  4294966972 |
|      16 | 0x0423      |        1059 |
|      17 | 0x136C9     |       79561 |
|      18 | 0x45F8      |       17912 |
|      19 | 0x0000      |           0 |
|      20 | 0x045E      |        1118 |
|      21 | 0x0029      |          41 |
|      22 | 0xFFFF0FB0  |  4294905776 |
|      23 | 0xFFFE504B  |  4294856779 |
|      24 | 0xFFFF25E9  |  4294911465 |
|      25 | 0xFFFE2E62  |  4294848098 |
|      26 | 0x00C7      |         199 |
|      27 | 0x000B      |          11 |
|      28 | 0xFFFF337D  |  4294914941 |
|      29 | 0xFFFE28D3  |  4294846675 |
|      30 | 0xFFFFFFEA  |  4294967274 |
|      31 | 0xBE71      |       48753 |

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

### Event 34

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
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 32 04 80 1F 00    7........2....
0010: 05 80 06 80 02 80 1F 01  6F 1E B4 42 04 01 00     ........o..B... 
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=87.304*, z=38.878*, y=0.480*, direction=282.5°*
  1: 0x000B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=82.511*, Z=48.266*, Y=0.480*
  3: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0019 [0x1E] EventEntity looks at Aphmau (ID: 17056436/0x010442B4) and starts talking
  6: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               32                 2
0020: 07 80 1F 00 08 80 09 80  02 80 1F 01 6F 1E B4 42  ............o..B
0030: 04 01 00                                          ...             
```

#### Opcodes

```
  0: 0x001F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=81.135*, Z=49.486*, Y=0.480*
  2: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x002D [0x1E] EventEntity looks at Aphmau (ID: 17056436/0x010442B4) and starts talking
  5: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          32 04 80 1F 00  0A 80 0B 80 0C 80 1F 01     2............
0040: 6F 1E B4 42 04 01 00                              o..B...         
```

#### Opcodes

```
  0: 0x0033 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0036 [0x1F] MOVE_ENTITY: EventEntity moves to X=80.148*, Z=29.559*, Y=-0.315*
  2: 0x003E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0040 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0041 [0x1E] EventEntity looks at Aphmau (ID: 17056436/0x010442B4) and starts talking
  5: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 49 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      37  0D 80 0E 80 0F 80 10 80         7........
0050: 32 04 80 1F 00 11 80 12  80 13 80 1F 01 6F 1E B1  2............o..
0060: 42 04 01 7B AC 42 04 01  5B 14 80 AC 42 04 01 AC  B..{.B..[...B...
0070: 42 04 01 66 67 68 30 00                           B..fgh0.        
```

#### Opcodes

```
  0: 0x0047 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=79.751*, z=27.478*, y=-0.324*, direction=93.1°*
  1: 0x0050 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x0053 [0x1F] MOVE_ENTITY: EventEntity moves to X=79.561*, Z=17.912*, Y=0.000*
  3: 0x005B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x005D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x005E [0x1E] EventEntity looks at Mihli Aliapoh (ID: 17056433/0x010442B1) and starts talking
  6: 0x0063 [0x7B] Rughadjeen (ID: 17056428/0x010442AC) stops talking
  7: 0x0068 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fgh0" with entities [Rughadjeen (ID: 17056428/0x010442AC), Rughadjeen (ID: 17056428/0x010442AC)], work=1118*
  8: 0x0077 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 31 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          32 15 80 1F 00 16 80 17          2.......
0080: 80 13 80 1F 01 6F 1F 00  18 80 19 80 1A 80 1F 01  .....o..........
0090: 6F 1E C0 42 04 01 00                              o..B...         
```

#### Opcodes

```
  0: 0x0078 [0x32] ExtData[1]->MainSpeed = 41* * 0.1
  1: 0x007B [0x1F] MOVE_ENTITY: EventEntity moves to X=-61.520*, Z=-110.517*, Y=0.000*
  2: 0x0083 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0085 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0086 [0x1F] MOVE_ENTITY: EventEntity moves to X=-55.831*, Z=-119.198*, Y=0.199*
  5: 0x008E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0090 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0091 [0x1E] EventEntity looks at Unnamed NPC (ID: 17056448/0x010442C0) and starts talking
  8: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      32  1B 80 1F 00 1C 80 1D 80         2........
00A0: 1A 80 1F 01 6F 1E C0 42  04 01 00                 ....o..B...     
```

#### Opcodes

```
  0: 0x0097 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x009A [0x1F] MOVE_ENTITY: EventEntity moves to X=-52.355*, Z=-120.621*, Y=0.199*
  2: 0x00A2 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00A5 [0x1E] EventEntity looks at Unnamed NPC (ID: 17056448/0x010442C0) and starts talking
  5: 0x00AA [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AB   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                   32 1B 80 1F 00             2....
00B0: 1E 80 1F 80 13 80 1F 01  6F 1E B1 42 04 01 00     ........o..B... 
```

#### Opcodes

```
  0: 0x00AB [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x00AE [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.022*, Z=48.753*, Y=0.000*
  2: 0x00B6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00B9 [0x1E] EventEntity looks at Mihli Aliapoh (ID: 17056433/0x010442B1) and starts talking
  5: 0x00BE [0x00] END_REQSTACK()
```
