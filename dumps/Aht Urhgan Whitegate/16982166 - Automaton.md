# 16982166 - Automaton

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 168 bytes                     |
| Total Events     | 5                             |
| References Count | 9                             |

## List of Events

| Event ID                  | Entrypoint   |   Size |   Instructions |
|---------------------------|--------------|--------|----------------|
| [65535](#event-65535)     | 0x0000       |      1 |              1 |
| [265](#event-265)         | 0x0001       |      1 |              1 |
| [65535.1](#event-65535-1) | 0x0002       |     45 |              6 |
| [266](#event-266)         | 0x002F       |      1 |              1 |
| [65535.2](#event-65535-2) | 0x0030       |     45 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x874C      |       34636 |
|       1 | 0xD8EC      |       55532 |
|       2 | 0xFFFFDDA0  |  4294958496 |
|       3 | 0x03F6      |        1014 |
|       4 | 0x0352      |         850 |
|       5 | 0x17497     |       95383 |
|       6 | 0xFFFF9BC0  |  4294941632 |
|       7 | 0xFFFFE890  |  4294961296 |
|       8 | 0x010C      |         268 |

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

### Event 265

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
| Data Size    | 45 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       33 01 37 00 80 01  80 02 80 03 80 80 F8 FF    3.7...........
0010: FF 7F 5B 04 80 96 20 03  01 96 20 03 01 70 61 30  ..[... ... ..pa0
0020: 31 53 96 20 03 01 96 20  03 01 70 61 30 31 00     1S. ... ..pa01. 
```

#### Opcodes

```
  0: 0x0002 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0004 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=34.636*, z=55.532*, y=-8.800*, direction=89.1°*
  2: 0x000D [0x80] LOAD_WAIT(entity=EventEntity)
  3: 0x0012 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pa01" with entities [Automaton (ID: 16982166/0x01032096), Automaton (ID: 16982166/0x01032096)], work=850*
  4: 0x0021 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pa01" with entities [Automaton (ID: 16982166/0x01032096), Automaton (ID: 16982166/0x01032096)]
  5: 0x002E [0x00] END_REQSTACK()
```

### Event 266

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               00                 .
```

#### Opcodes

```
  0: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 45 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 33 01 37 05 80 06 80 07  80 08 80 80 F8 FF FF 7F  3.7.............
0040: 5B 04 80 96 20 03 01 96  20 03 01 70 61 30 31 53  [... ... ..pa01S
0050: 96 20 03 01 96 20 03 01  70 61 30 31 00           . ... ..pa01.   
```

#### Opcodes

```
  0: 0x0030 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0032 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=95.383*, z=-25.664*, y=-6.000*, direction=23.6°*
  2: 0x003B [0x80] LOAD_WAIT(entity=EventEntity)
  3: 0x0040 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pa01" with entities [Automaton (ID: 16982166/0x01032096), Automaton (ID: 16982166/0x01032096)], work=850*
  4: 0x004F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pa01" with entities [Automaton (ID: 16982166/0x01032096), Automaton (ID: 16982166/0x01032096)]
  5: 0x005C [0x00] END_REQSTACK()
```
