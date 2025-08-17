# 17776701 - Auchefort

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 200 bytes             |
| Total Events     | 4                     |
| References Count | 19                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [207](#event-207)        | 0x0001       |     22 |              4 |
| [65535.1](#event-655351) | 0x0017       |     32 |              8 |
| [65535.2](#event-655352) | 0x0037       |     36 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF0674  |  4294903412 |
|       1 | 0x46E4      |       18148 |
|       2 | 0x03E8      |        1000 |
|       3 | 0x0379      |         889 |
|       4 | 0x001E      |          30 |
|       5 | 0x0028      |          40 |
|       6 | 0xFFFF03F6  |  4294902774 |
|       7 | 0x32A5      |       12965 |
|       8 | 0xFFFF07BC  |  4294903740 |
|       9 | 0x2A7A      |       10874 |
|      10 | 0xFFFF39D6  |  4294916566 |
|      11 | 0x6139      |       24889 |
|      12 | 0x03E7      |         999 |
|      13 | 0xFFFF45BD  |  4294919613 |
|      14 | 0x9029      |       36905 |
|      15 | 0xFFFFFF39  |  4294967097 |
|      16 | 0xFFFF36F3  |  4294915827 |
|      17 | 0xD157      |       53591 |
|      18 | 0x0000      |           0 |

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

### Event 207

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 94  01 F8 FF FF 7F 37 00 80   ............7..
0010: 01 80 02 80 03 80 00                              .......         
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-63.884*, z=18.148*, y=1.000*, direction=78.1°*
  3: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 32 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      1C  04 80 32 05 80 1F 00 06         ...2.....
0020: 80 07 80 02 80 1F 01 1F  00 08 80 09 80 02 80 1F  ................
0030: 01 1E 39 40 0F 01 00                              ..9@...         
```

#### Opcodes

```
  0: 0x0017 [0x1C] WAIT(30* ticks)
  1: 0x001A [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x001D [0x1F] MOVE_ENTITY: EventEntity moves to X=-64.522*, Z=12.965*, Y=1.000*
  3: 0x0025 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=-63.556*, Z=10.874*, Y=1.000*
  5: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0031 [0x1E] EventEntity looks at Unnamed NPC (ID: 17776697/0x010F4039) and starts talking
  7: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 36 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      32  05 80 1F 00 0A 80 0B 80         2........
0040: 0C 80 1F 01 1F 00 0D 80  0E 80 0F 80 1F 01 1F 00  ................
0050: 10 80 11 80 12 80 1F 01  22 01 00                 ........"..     
```

#### Opcodes

```
  0: 0x0037 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003A [0x1F] MOVE_ENTITY: EventEntity moves to X=-50.730*, Z=24.889*, Y=0.999*
  2: 0x0042 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0044 [0x1F] MOVE_ENTITY: EventEntity moves to X=-47.683*, Z=36.905*, Y=-0.199*
  4: 0x004C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x004E [0x1F] MOVE_ENTITY: EventEntity moves to X=-51.469*, Z=53.591*, Y=0.000*
  6: 0x0056 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0058 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  8: 0x005A [0x00] END_REQSTACK()
```
