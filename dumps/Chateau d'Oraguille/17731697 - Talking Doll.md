# 17731697 - Talking Doll

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Chateau d'Oraguille (ID: 233) |
| Block Size       | 120 bytes                     |
| Total Events     | 6                             |
| References Count | 4                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [604](#event-604)        | 0x0001       |      7 |              2 |
| [605](#event-605)        | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |     10 |              2 |
| [65535.2](#event-655352) | 0x0019       |     16 |              2 |
| [65535.3](#event-655353) | 0x0029       |     22 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0080      |         128 |
|       1 | 0x0064      |         100 |
|       2 | 0x00FC      |         252 |
|       3 | 0x001E      |          30 |

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

### Event 604

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 605

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               6C                 l
0010: F8 FF FF 7F 00 80 01 80  00                       .........       
```

#### Opcodes

```
  0: 0x000F [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=100*)
  1: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             5B 02 80 F8 FF FF 7F           [......
0020: F8 FF FF 7F 62 72 75 30  00                       ....bru0.       
```

#### Opcodes

```
  0: 0x0019 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bru0" with entities [EventEntity, EventEntity], work=252*
  1: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             53 F8 FF FF 7F F8 FF           S......
0030: FF 7F 62 72 75 30 5E 69  64 6C 30 1C 03 80 00     ..bru0^idl0.... 
```

#### Opcodes

```
  0: 0x0029 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bru0" with entities [EventEntity, EventEntity]
  1: 0x0036 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x003B [0x1C] WAIT(30* ticks)
  3: 0x003E [0x00] END_REQSTACK()
```
