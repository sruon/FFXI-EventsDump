# 17391833 - Shadow of Darkness

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Monastic Cavern (ID: 150) |
| Block Size       | 164 bytes                 |
| Total Events     | 10                        |
| References Count | 8                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [0](#event-0)            | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |      1 |              1 |
| [65535](#event-65535)    | 0x0002       |     16 |              3 |
| [65535.1](#event-655351) | 0x0012       |     25 |              4 |
| [65535.2](#event-655352) | 0x002B       |     10 |              2 |
| [65535.3](#event-655353) | 0x0035       |      5 |              3 |
| [65535.4](#event-655354) | 0x003A       |      5 |              3 |
| [65535.5](#event-655355) | 0x003F       |      5 |              3 |
| [65535.6](#event-655356) | 0x0044       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0040      |          64 |
|       3 | 0x012C      |         300 |
|       4 | 0x1C7A      |        7290 |
|       5 | 0x1C7B      |        7291 |
|       6 | 0x1C7D      |        7293 |
|       7 | 0x1C7E      |        7294 |

## String References

- **7290**: You are too late. I have awoken.
- **7291**: Your rage, cowardice, envy, arrogance, and apathy... From these I will spread the bane of Vana'diel.
- **7293**: Your kind has awoken me...and this time, you will be destroyed!
- **7294**: You cannot stop me. Vana'diel will be a grave for you and all your kind!

## Events

### Event 0

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

### Event 1

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

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       2F 00 D9 60 09 01  6C F8 FF FF 7F 00 80 01    /..`..l.......
0010: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0002 [0x2F] Shadow of Darkness (ID: 17391833/0x010960D9)->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0008 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  2: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 25 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       22 00 2C F8 FF FF  7F F8 FF FF 7F 69 6E 69    ".,........ini
0020: 74 6C F8 FF FF 7F 02 80  03 80 00                 tl.........     
```

#### Opcodes

```
  0: 0x0012 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0014 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "init" with entities [EventEntity, EventEntity]
  2: 0x0021 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=64*, fade_time=300*)
  3: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   6C F8 FF FF 7F             l....
0030: 00 80 03 80 00                                    .....           
```

#### Opcodes

```
  0: 0x002B [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=300*)
  1: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0035  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                1D 04 80  23 00                         ...#.      
```

#### Opcodes

```
  0: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=7290*)
    → "You are too late. I have awoken."
  1: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003A  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                1D 05 80 23 00               ...#. 
```

#### Opcodes

```
  0: 0x003A [0x1D] PRINT_EVENT_MESSAGE(message_id=7291*)
    → "Your rage, cowardice, envy, arrogance, and apathy... From these I will spread the bane of Vana'diel."
  1: 0x003D [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x003E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003F  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               1D                 .
0040: 06 80 23 00                                       ..#.            
```

#### Opcodes

```
  0: 0x003F [0x1D] PRINT_EVENT_MESSAGE(message_id=7293*)
    → "Your kind has awoken me...and this time, you will be destroyed!"
  1: 0x0042 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             1D 07 80 23  00                           ...#.       
```

#### Opcodes

```
  0: 0x0044 [0x1D] PRINT_EVENT_MESSAGE(message_id=7294*)
    → "You cannot stop me. Vana'diel will be a grave for you and all your kind!"
  1: 0x0047 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0048 [0x00] END_REQSTACK()
```
