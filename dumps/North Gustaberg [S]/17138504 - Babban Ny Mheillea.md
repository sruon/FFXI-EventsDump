# 17138504 - Babban Ny Mheillea

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | North Gustaberg [S] (ID: 88) |
| Block Size       | 188 bytes                    |
| Total Events     | 6                            |
| References Count | 13                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [114](#event-114)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     17 |              6 |
| [65535.2](#event-655352) | 0x0013       |     32 |              9 |
| [65535.3](#event-655353) | 0x0033       |     29 |              3 |
| [65535.4](#event-655354) | 0x0050       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0006      |           6 |
|       1 | 0x5D7FB     |      382971 |
|       2 | 0x79757     |      497495 |
|       3 | 0x7E28      |       32296 |
|       4 | 0x0028      |          40 |
|       5 | 0x5C691     |      378513 |
|       6 | 0x7B17E     |      504190 |
|       7 | 0x7F46      |       32582 |
|       8 | 0x0871      |        2161 |
|       9 | 0x0010      |          16 |
|      10 | 0x4D73A     |      317242 |
|      11 | 0x62446     |      402502 |
|      12 | 0x1F0A      |        7946 |

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

### Event 114

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
| Data Size    | 17 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       61 00 32 00 80 1F  00 01 80 02 80 03 80 1F    a.2...........
0010: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0002 [0x61] EventEntity->Render.Flags2 &= ~0x00000001
  1: 0x0004 [0x32] ExtData[1]->MainSpeed = 6* * 0.1
  2: 0x0007 [0x1F] MOVE_ENTITY: EventEntity moves to X=382.971*, Z=497.495*, Y=32.296*
  3: 0x000F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0011 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 32 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          61 00 32 04 80  1F 00 05 80 06 80 07 80     a.2..........
0020: 1F 01 6F 4A F8 FF FF 7F  4B 83 05 01 6F 76 F8 FF  ..oJ....K...ov..
0030: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x0013 [0x61] EventEntity->Render.Flags2 &= ~0x00000001
  1: 0x0015 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x0018 [0x1F] MOVE_ENTITY: EventEntity moves to X=378.513*, Z=504.190*, Y=32.582*
  3: 0x0020 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0022 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0023 [0x4A] EventEntity looks at Camlin (ID: 17138507/0x0105834B)
  6: 0x002C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x002D [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  8: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          5B 08 80 48 83  05 01 48 83 05 01 74 6C     [..H...H...tl
0040: 6B 30 53 48 83 05 01 48  83 05 01 74 6C 6B 30 00  k0SH...H...tlk0.
```

#### Opcodes

```
  0: 0x0033 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Babban Ny Mheillea (ID: 17138504/0x01058348), Babban Ny Mheillea (ID: 17138504/0x01058348)], work=2161*
  1: 0x0042 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [Babban Ny Mheillea (ID: 17138504/0x01058348), Babban Ny Mheillea (ID: 17138504/0x01058348)]
  2: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 32 09 80 1F 00 0A 80 0B  80 0C 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0050 [0x32] ExtData[1]->MainSpeed = 16* * 0.1
  1: 0x0053 [0x1F] MOVE_ENTITY: EventEntity moves to X=317.242*, Z=402.502*, Y=7.946*
  2: 0x005B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005D [0x00] END_REQSTACK()
```
