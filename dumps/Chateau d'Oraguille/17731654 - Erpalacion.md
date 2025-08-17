# 17731654 - Erpalacion

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Chateau d'Oraguille (ID: 233) |
| Block Size       | 236 bytes                     |
| Total Events     | 8                             |
| References Count | 11                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [121](#event-121)        | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     53 |             10 |
| [68](#event-68)          | 0x0040       |      1 |              1 |
| [65535.2](#event-655352) | 0x0041       |     12 |              3 |
| [65535.3](#event-655353) | 0x004D       |     29 |              3 |
| [65535.4](#event-655354) | 0x006A       |     29 |              3 |
| [65535.5](#event-655355) | 0x0087       |      9 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000B      |          11 |
|       1 | 0x98E0      |       39136 |
|       2 | 0xFFFFF381  |  4294964097 |
|       3 | 0x0BFA      |        3066 |
|       4 | 0x001D      |          29 |
|       5 | 0x003C      |          60 |
|       6 | 0x0400      |        1024 |
|       7 | 0x000D      |          13 |
|       8 | 0x0000      |           0 |
|       9 | 0x7D87      |       32135 |
|      10 | 0xFFFFF449  |  4294964297 |

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

### Event 121

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.011*, z=39.136*, y=-3.199*, direction=269.5°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 53 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   66 04 80 46 90             f..F.
0010: 0E 01 46 90 0E 01 73 68  61 31 53 46 90 0E 01 46  ..F...sha1SF...F
0020: 90 0E 01 73 68 61 31 1C  05 80 39 06 80 1C 05 80  ...sha1...9.....
0030: 32 07 80 1F 00 08 80 09  80 0A 80 1F 01 22 01 00  2............"..
```

#### Opcodes

```
  0: 0x000B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [Erpalacion (ID: 17731654/0x010E9046), Erpalacion (ID: 17731654/0x010E9046)], work=29*
  1: 0x001A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [Erpalacion (ID: 17731654/0x010E9046), Erpalacion (ID: 17731654/0x010E9046)]
  2: 0x0027 [0x1C] WAIT(60* ticks)
  3: 0x002A [0x39] SET_ENTITY_DIRECTION(direction=5.6°*)
  4: 0x002D [0x1C] WAIT(60* ticks)
  5: 0x0030 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  6: 0x0033 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.000*, Z=32.135*, Y=-2.999*
  7: 0x003B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x003D [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  9: 0x003F [0x00] END_REQSTACK()
```

### Event 68

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0040  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0040 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0041   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    22 00 37 00 80 01 80  02 80 03 80 00            ".7.........   
```

#### Opcodes

```
  0: 0x0041 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0043 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.011*, z=39.136*, y=-3.199*, direction=269.5°*
  2: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         66 04 80               f..
0050: 46 90 0E 01 46 90 0E 01  73 68 61 31 53 46 90 0E  F...F...sha1SF..
0060: 01 46 90 0E 01 73 68 61  31 00                    .F...sha1.      
```

#### Opcodes

```
  0: 0x004D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [Erpalacion (ID: 17731654/0x010E9046), Erpalacion (ID: 17731654/0x010E9046)], work=29*
  1: 0x005C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [Erpalacion (ID: 17731654/0x010E9046), Erpalacion (ID: 17731654/0x010E9046)]
  2: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                66 04 80 F8 FF FF            f.....
0070: 7F F8 FF FF 7F 74 6C 6B  30 53 F8 FF FF 7F F8 FF  .....tlk0S......
0080: FF 7F 74 6C 6B 30 00                              ..tlk0.         
```

#### Opcodes

```
  0: 0x006A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  1: 0x0079 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0087  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      5E  69 64 6C 30 1C 05 80 00         ^idl0....
```

#### Opcodes

```
  0: 0x0087 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x008C [0x1C] WAIT(60* ticks)
  2: 0x008F [0x00] END_REQSTACK()
```
