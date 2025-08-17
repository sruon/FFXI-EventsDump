# 17248901 - Noh Ramyoh

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | West Sarutabaruta (ID: 115) |
| Block Size       | 192 bytes                   |
| Total Events     | 7                           |
| References Count | 7                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      1 |              1 |
| [65535.2](#event-655352) | 0x0002       |      1 |              1 |
| [65535.3](#event-655353) | 0x0003       |      1 |              1 |
| [65535.4](#event-655354) | 0x0004       |     19 |              3 |
| [65535.5](#event-655355) | 0x0017       |     61 |             13 |
| [65535.6](#event-655356) | 0x0054       |     34 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x18BE      |        6334 |
|       1 | 0x590A      |       22794 |
|       2 | 0xFFFFFC19  |  4294966297 |
|       3 | 0x0A20      |        2592 |
|       4 | 0x001E      |          30 |
|       5 | 0x2674      |        9844 |
|       6 | 0x5333      |       21299 |

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

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             37 00 80 01  80 02 80 03 80 4A 85 32      7........J.2
0010: 07 01 81 32 07 01 00                              ...2...         
```

#### Opcodes

```
  0: 0x0004 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=6.334*, z=22.794*, y=-0.999*, direction=227.8°*
  1: 0x000D [0x4A] Noh Ramyoh (ID: 17248901/0x01073285) looks at Khoto Rokkorah (ID: 17248897/0x01073281)
  2: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 61 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      4A  85 32 07 01 86 32 07 01         J.2...2..
0020: 6F 76 85 32 07 01 4A 85  32 07 01 83 32 07 01 6F  ov.2..J.2...2..o
0030: 76 85 32 07 01 4A 85 32  07 01 87 32 07 01 6F 76  v.2..J.2...2..ov
0040: 85 32 07 01 4A 85 32 07  01 88 32 07 01 6F 76 85  .2..J.2...2..ov.
0050: 32 07 01 00                                       2...            
```

#### Opcodes

```
  0: 0x0017 [0x4A] Noh Ramyoh (ID: 17248901/0x01073285) looks at Cotta-Lotta (ID: 17248902/0x01073286)
  1: 0x0020 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0021 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Noh Ramyoh (ID: 17248901/0x01073285) Render.Flags0 and Render.Flags3 conditions are met
  3: 0x0026 [0x4A] Noh Ramyoh (ID: 17248901/0x01073285) looks at Kuppo-Pippo (ID: 17248899/0x01073283)
  4: 0x002F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0030 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Noh Ramyoh (ID: 17248901/0x01073285) Render.Flags0 and Render.Flags3 conditions are met
  6: 0x0035 [0x4A] Noh Ramyoh (ID: 17248901/0x01073285) looks at Tacca-Picca (ID: 17248903/0x01073287)
  7: 0x003E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x003F [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Noh Ramyoh (ID: 17248901/0x01073285) Render.Flags0 and Render.Flags3 conditions are met
  9: 0x0044 [0x4A] Noh Ramyoh (ID: 17248901/0x01073285) looks at Rahmi Yamilahto (ID: 17248904/0x01073288)
 10: 0x004D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 11: 0x004E [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Noh Ramyoh (ID: 17248901/0x01073285) Render.Flags0 and Render.Flags3 conditions are met
 12: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 34 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             4A 85 32 07  01 81 32 07 01 32 04 80      J.2...2..2..
0060: 1F 00 05 80 06 80 02 80  1F 01 6F 79 00 85 32 07  ..........oy..2.
0070: 01 81 32 07 01 00                                 ..2...          
```

#### Opcodes

```
  0: 0x0054 [0x4A] Noh Ramyoh (ID: 17248901/0x01073285) looks at Khoto Rokkorah (ID: 17248897/0x01073281)
  1: 0x005D [0x32] ExtData[1]->MainSpeed = 30* * 0.1
  2: 0x0060 [0x1F] MOVE_ENTITY: EventEntity moves to X=9.844*, Z=21.299*, Y=-0.999*
  3: 0x0068 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x006A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x006B [0x79] Noh Ramyoh (ID: 17248901/0x01073285) looks at Khoto Rokkorah (ID: 17248897/0x01073281) (Basic look)
  6: 0x0075 [0x00] END_REQSTACK()
```
