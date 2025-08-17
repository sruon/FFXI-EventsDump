# 17731672 - Travialce

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Chateau d'Oraguille (ID: 233) |
| Block Size       | 276 bytes                     |
| Total Events     | 7                             |
| References Count | 14                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [564](#event-564)        | 0x0001       |     27 |              5 |
| [65535.1](#event-655351) | 0x001C       |     15 |              5 |
| [65535.2](#event-655352) | 0x002B       |     29 |              3 |
| [65535.3](#event-655353) | 0x0048       |     15 |              3 |
| [65535.4](#event-655354) | 0x0057       |     89 |             18 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0xFFFFFCF4  |  4294966516 |
|       2 | 0x0000      |           0 |
|       3 | 0x0E4B      |        3659 |
|       4 | 0xFFFFF830  |  4294965296 |
|       5 | 0x000D      |          13 |
|       6 | 0x0015      |          21 |
|       7 | 0xFFFFF2F4  |  4294963956 |
|       8 | 0x09F4      |        2548 |
|       9 | 0x0078      |         120 |
|      10 | 0x005A      |          90 |
|      11 | 0xFFFFE1A9  |  4294959529 |
|      12 | 0xFFFFF79F  |  4294965151 |
|      13 | 0x00B4      |         180 |

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

### Event 564

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 27 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 03 00 00 04 80 1A   7..............
0010: 6C 00 37 01 00 02 00 03  00 04 00 00              l.7.........    
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.050*, z=-0.780*, y=0.000*, direction=321.6°*
  1: 0x000A [0x03] ExtData[1]->WorkLocal[0] = 4294965296*
  2: 0x000F [0x1A] CALL_SUBROUTINE(address=0x006C)
  3: 0x0012 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[1], z=ExtData[1]->WorkLocal[2], y=ExtData[1]->WorkLocal[3], direction=ExtData[1]->WorkLocal[4]
  4: 0x001B [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      32 05 80 1F              2...
0020: 00 00 80 01 80 02 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x001C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001F [0x1F] MOVE_ENTITY: EventEntity moves to X=0.050*, Z=-0.780*, Y=0.000*
  2: 0x0027 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0029 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   66 06 80 F8 FF             f....
0030: FF 7F F8 FF FF 7F 73 6C  30 30 53 F8 FF FF 7F F8  ......sl00S.....
0040: FF FF 7F 73 6C 30 30 00                           ...sl00.        
```

#### Opcodes

```
  0: 0x002B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sl00" with entities [EventEntity, EventEntity], work=21*
  1: 0x003A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sl00" with entities [EventEntity, EventEntity]
  2: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          7B F8 FF FF 7F 37 07 80          {....7..
0050: 08 80 02 80 09 80 00                              .......         
```

#### Opcodes

```
  0: 0x0048 [0x7B] EventEntity stops talking
  1: 0x004D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-3.340*, z=2.548*, y=0.000*, direction=10.5°*
  2: 0x0056 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 89 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      1C  0A 80 32 05 80 31 00 0B         ...2..1..
0060: 80 0C 80 02 80 0D 80 31  01 22 01 00 3B F8 FF FF  .......1."..;...
0070: 7F 01 00 02 00 03 00 3A  F8 FF FF 7F 04 00 17 05  .......:........
0080: 00 04 00 00 00 16 06 00  04 00 00 00 07 01 00 05  ................
0090: 00 07 02 00 06 00 1B 17  05 00 04 00 00 00 16 06  ................
00A0: 00 04 00 00 00 07 01 00  05 00 07 02 00 06 00 1B  ................
```

#### Opcodes

```
  0: 0x0057 [0x1C] WAIT(90* ticks)
  1: 0x005A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x005D [0x31] UPDATE_ENTITY_POSITION: Set EventEntity goal position to X=-7.767*, Z=-2.145*, Y=0.000*, Time=180*
  3: 0x0067 [0x31] UPDATE_ENTITY_POSITION: Move EventEntity towards goal position
  4: 0x0069 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  5: 0x006B [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x006C [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
     0x0077 [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[4])
     0x007E [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0085 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x008C [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x0091 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x0096 [0x1B] RETURN
     0x0097 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x009E [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x00A5 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x00AA [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x00AF [0x1B] RETURN
```
