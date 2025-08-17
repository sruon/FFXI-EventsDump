# 17396261 - Ulbrik-Mulbrok

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Castle Oztroja (ID: 151) |
| Block Size       | 220 bytes                |
| Total Events     | 8                        |
| References Count | 13                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [99](#event-99)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |      7 |              3 |
| [65535.2](#event-655352) | 0x0009       |      7 |              3 |
| [65535.3](#event-655353) | 0x0010       |     29 |              3 |
| [65535.4](#event-655354) | 0x002D       |     29 |              3 |
| [65535.5](#event-655355) | 0x004A       |     14 |              4 |
| [65535.6](#event-655356) | 0x0058       |     29 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x0031      |          49 |
|       3 | 0x000D      |          13 |
|       4 | 0xFFFEE692  |  4294895250 |
|       5 | 0xE908      |       59656 |
|       6 | 0xFFFF0E9F  |  4294905503 |
|       7 | 0x0009      |           9 |
|       8 | 0x0041      |          65 |
|       9 | 0x0050      |          80 |
|      10 | 0xFFFF10A6  |  4294906022 |
|      11 | 0xEF14      |       61204 |
|      12 | 0xFFFF0CD6  |  4294905046 |

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

### Event 99

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       AB 03 AC 01 00 80  00                         .......       
```

#### Opcodes

```
  0: 0x0002 [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0004 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x0008 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0009  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             AC 01 01 80 AB 04 00           .......
```

#### Opcodes

```
  0: 0x0009 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x000D [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 66 02 80 F8 FF FF 7F F8  FF FF 7F 73 68 61 30 53  f..........sha0S
0020: F8 FF FF 7F F8 FF FF 7F  73 68 61 30 00           ........sha0.   
```

#### Opcodes

```
  0: 0x0010 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=49*
  1: 0x001F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha0" with entities [EventEntity, EventEntity]
  2: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         66 02 80               f..
0030: F8 FF FF 7F F8 FF FF 7F  73 68 61 31 53 F8 FF FF  ........sha1S...
0040: 7F F8 FF FF 7F 73 68 61  31 00                    .....sha1.      
```

#### Opcodes

```
  0: 0x002D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha1" with entities [EventEntity, EventEntity], work=49*
  1: 0x003C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sha1" with entities [EventEntity, EventEntity]
  2: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                32 03 80 1F 00 04            2.....
0050: 80 05 80 06 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x004A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x004D [0x1F] MOVE_ENTITY: EventEntity moves to X=-72.046*, Z=59.656*, Y=-61.793*
  2: 0x0055 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 29 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          AD 02 07 80 25 72 09 01          ....%r..
0060: 25 72 09 01 1C 08 80 32  09 80 1F 00 0A 80 0B 80  %r.....2........
0070: 0C 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0058 [0xAD] DUAL_ENTITY_SCHEDULER_HANDLER: Execute sub-case 2 with entities [Ulbrik-Mulbrok (ID: 17396261/0x01097225), Ulbrik-Mulbrok (ID: 17396261/0x01097225)], work=9*
  1: 0x0064 [0x1C] WAIT(65* ticks)
  2: 0x0067 [0x32] ExtData[1]->MainSpeed = 80* * 0.1
  3: 0x006A [0x1F] MOVE_ENTITY: EventEntity moves to X=-61.274*, Z=61.204*, Y=-62.250*
  4: 0x0072 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0074 [0x00] END_REQSTACK()
```
