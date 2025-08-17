# 17596817 - Rainemard

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Garlaige Citadel (ID: 200) |
| Block Size       | 236 bytes                  |
| Total Events     | 9                          |
| References Count | 12                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [14](#event-14)          | 0x0001       |     15 |              4 |
| [65535.1](#event-655351) | 0x0010       |     12 |              4 |
| [65535.2](#event-655352) | 0x001C       |     17 |              5 |
| [65535.3](#event-655353) | 0x002D       |     16 |              4 |
| [65535.4](#event-655354) | 0x003D       |     16 |              2 |
| [65535.5](#event-655355) | 0x004D       |     13 |              3 |
| [65535.6](#event-655356) | 0x005A       |     16 |              2 |
| [65535.7](#event-655357) | 0x006A       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFD8945  |  4294805829 |
|       1 | 0x36CC3     |      224451 |
|       2 | 0x0000      |           0 |
|       3 | 0x07C8      |        1992 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFD7F8E  |  4294803342 |
|       6 | 0xFFFD6D30  |  4294798640 |
|       7 | 0x3824D     |      229965 |
|       8 | 0xFFFD59F1  |  4294793713 |
|       9 | 0x38268     |      229992 |
|      10 | 0x0014      |          20 |
|      11 | 0x001E      |          30 |

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

### Event 14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    33 01 37 00 80 01 80  02 80 03 80 32 04 80 00   3.7........2...
```

#### Opcodes

```
  0: 0x0001 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0003 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-161.467*, z=224.451*, y=0.000*, direction=175.1°*
  2: 0x000C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 1F 00 05 80 01 80 02 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x0010 [0x1F] MOVE_ENTITY: EventEntity moves to X=-163.954*, Z=224.451*, Y=0.000*
  1: 0x0018 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x001A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x001B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      1F 00 06 80              ....
0020: 07 80 02 80 1F 01 6F 1E  F0 FF FF 7F 00           ......o......   
```

#### Opcodes

```
  0: 0x001C [0x1F] MOVE_ENTITY: EventEntity moves to X=-168.656*, Z=229.965*, Y=0.000*
  1: 0x0024 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0026 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0027 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         7B F8 FF               {..
0030: FF 7F 1F 00 08 80 09 80  02 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x002D [0x7B] EventEntity stops talking
  1: 0x0032 [0x1F] MOVE_ENTITY: EventEntity moves to X=-173.583*, Z=229.992*, Y=0.000*
  2: 0x003A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         66 0A 80               f..
0040: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 00           ........tlk0.   
```

#### Opcodes

```
  0: 0x003D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  1: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         6B 69 64               kid
0050: 6C 30 F8 FF FF 7F 1C 0B  80 00                    l0........      
```

#### Opcodes

```
  0: 0x004D [0x6B] STOP_AND_IDLE: EventEntity stops current action and resets to idle (animation="idl0")
  1: 0x0056 [0x1C] WAIT(30* ticks)
  2: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                66 0A 80 F8 FF FF            f.....
0060: 7F F8 FF FF 7F 74 68 6B  31 00                    .....thk1.      
```

#### Opcodes

```
  0: 0x005A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=20*
  1: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                66 0A 80 F8 FF FF            f.....
0070: 7F F8 FF FF 7F 74 68 6B  32 53 F8 FF FF 7F F8 FF  .....thk2S......
0080: FF 7F 74 68 6B 32 00                              ..thk2.         
```

#### Opcodes

```
  0: 0x006A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=20*
  1: 0x0079 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  2: 0x0086 [0x00] END_REQSTACK()
```
