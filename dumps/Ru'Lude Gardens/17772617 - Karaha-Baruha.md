# 17772617 - Karaha-Baruha

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 180 bytes                 |
| Total Events     | 11                        |
| References Count | 13                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10010](#event-10010)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     14 |              4 |
| [65535.2](#event-655352) | 0x0010       |     14 |              4 |
| [65535.3](#event-655353) | 0x001E       |      5 |              3 |
| [65535.4](#event-655354) | 0x0023       |      5 |              3 |
| [65535.5](#event-655355) | 0x0028       |      5 |              3 |
| [65535.6](#event-655356) | 0x002D       |      5 |              3 |
| [65535.7](#event-655357) | 0x0032       |      5 |              3 |
| [65535.8](#event-655358) | 0x0037       |      5 |              3 |
| [65535.9](#event-655359) | 0x003C       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x232BF     |      144063 |
|       2 | 0xFFFFB2F4  |  4294947572 |
|       3 | 0x32C7      |       12999 |
|       4 | 0x233EB     |      144363 |
|       5 | 0xFFFFBD98  |  4294950296 |
|       6 | 0x2AE6      |       10982 |
|       7 | 0x2AE7      |       10983 |
|       8 | 0x2AE8      |       10984 |
|       9 | 0x2AEA      |       10986 |
|      10 | 0x2AEE      |       10990 |
|      11 | 0x2AEF      |       10991 |
|      12 | 0x2AF0      |       10992 |

## String References

- **10982**: Yes, I would like to name this magic "summoning."
- **10983**: The divine texts depict it in the form of the Star Sibyl commanding a great beast.
- **10984**: At any rate, we are very close. Soon, the magic of summoning will be complete.
- **10986**: Are you uneasy, Your Holiness?
- **10990**: Place your trust in me, Your Holiness. Windurst shall escape its fate of ruin.
- **10991**: The Book of the Gods has taught me everything.
- **10992**: It told me the meaning of the tower and the fountain. And it has taught me how to command the greatest of beasts.

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

### Event 10010

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
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=144.063*, Z=-19.724*, Y=12.999*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 32 00 80 1F 00 04 80 05  80 03 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0010 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0013 [0x1F] MOVE_ENTITY: EventEntity moves to X=144.363*, Z=-17.000*, Y=12.999*
  2: 0x001B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            1D 06                ..
0020: 80 23 00                                          .#.             
```

#### Opcodes

```
  0: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=10982*)
    → "Yes, I would like to name this magic "summoning.""
  1: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0023  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          1D 07 80 23 00                              ...#.        
```

#### Opcodes

```
  0: 0x0023 [0x1D] PRINT_EVENT_MESSAGE(message_id=10983*)
    → "The divine texts depict it in the form of the Star Sibyl commanding a great beast."
  1: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0027 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0028  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          1D 08 80 23 00                   ...#.   
```

#### Opcodes

```
  0: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=10984*)
    → "At any rate, we are very close. Soon, the magic of summoning will be complete."
  1: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002D  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         1D 09 80               ...
0030: 23 00                                             #.              
```

#### Opcodes

```
  0: 0x002D [0x1D] PRINT_EVENT_MESSAGE(message_id=10986*)
    → "Are you uneasy, Your Holiness?"
  1: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0032  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       1D 0A 80 23 00                                ...#.         
```

#### Opcodes

```
  0: 0x0032 [0x1D] PRINT_EVENT_MESSAGE(message_id=10990*)
    → "Place your trust in me, Your Holiness. Windurst shall escape its fate of ruin."
  1: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0037  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      1D  0B 80 23 00                     ...#.    
```

#### Opcodes

```
  0: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=10991*)
    → "The Book of the Gods has taught me everything."
  1: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003C  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      1D 0C 80 23              ...#
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x003C [0x1D] PRINT_EVENT_MESSAGE(message_id=10992*)
    → "It told me the meaning of the tower and the fountain. And it has taught me how to command the greatest of beasts."
  1: 0x003F [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0040 [0x00] END_REQSTACK()
```
