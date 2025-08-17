# 17756504 - Shantotto

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 188 bytes                |
| Total Events     | 8                        |
| References Count | 10                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     35 |              4 |
| [65535.2](#event-655352) | 0x0024       |      7 |              3 |
| [65535.3](#event-655353) | 0x002B       |      7 |              3 |
| [569](#event-569)        | 0x0032       |      7 |              2 |
| [575](#event-575)        | 0x0039       |      1 |              1 |
| [65535.4](#event-655354) | 0x003A       |     21 |              2 |
| [65535.5](#event-655355) | 0x004F       |     21 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000F      |          15 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x0005      |           5 |
|       4 | 0x0004      |           4 |
|       5 | 0x002E      |          46 |
|       6 | 0x0385      |         901 |
|       7 | 0x0006      |           6 |
|       8 | 0x0013      |          19 |
|       9 | 0x0259      |         601 |

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 35 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    81 00 F8 FF FF 7F 66  00 80 F8 FF FF 7F F8 FF   ......f........
0010: FF 7F 73 74 64 30 53 F8  FF FF 7F F8 FF FF 7F 73  ..std0S........s
0020: 74 64 30 00                                       td0.            
```

#### Opcodes

```
  0: 0x0001 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0007 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "std0" with entities [EventEntity, EventEntity], work=15*
  2: 0x0016 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "std0" with entities [EventEntity, EventEntity]
  3: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             AB 03 AC 01  01 80 00                     .......     
```

#### Opcodes

```
  0: 0x0024 [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0026 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002B  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   AC 01 02 80 AB             .....
0030: 04 00                                             ..              
```

#### Opcodes

```
  0: 0x002B [0xAC] EventEntity->StatusEvent = 0*
  1: 0x002F [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x0031 [0x00] END_REQSTACK()
```

### Event 569

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0032  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       92 01 F8 FF FF 7F  00                         .......       
```

#### Opcodes

```
  0: 0x0032 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 575

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0039  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             00                             .      
```

#### Opcodes

```
  0: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                B6 0B 03 80 04 80            ......
0040: 02 80 05 80 05 80 05 80  05 80 06 80 02 80 00     ............... 
```

#### Opcodes

```
  0: 0x003A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=4*, head=0*, body=46*, hands=46*, legs=46*, feet=46*, main=901*, sub=0*)
  1: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               B6                 .
0050: 0B 07 80 07 80 02 80 08  80 08 80 08 80 08 80 09  ................
0060: 80 02 80 00                                       ....            
```

#### Opcodes

```
  0: 0x004F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=6*, hair=6*, head=0*, body=19*, hands=19*, legs=19*, feet=19*, main=601*, sub=0*)
  1: 0x0063 [0x00] END_REQSTACK()
```
