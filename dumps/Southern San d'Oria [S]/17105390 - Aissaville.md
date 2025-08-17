# 17105390 - Aissaville

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 120 bytes                        |
| Total Events     | 11                               |
| References Count | 2                                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [605](#event-605)     | 0x0001       |     41 |              7 |
| [55](#event-55)       | 0x002A       |      1 |              1 |
| [86](#event-86)       | 0x002B       |      1 |              1 |
| [87](#event-87)       | 0x002C       |      1 |              1 |
| [89](#event-89)       | 0x002D       |      1 |              1 |
| [123](#event-123)     | 0x002E       |      1 |              1 |
| [127](#event-127)     | 0x002F       |      1 |              1 |
| [148](#event-148)     | 0x0030       |      1 |              1 |
| [186](#event-186)     | 0x0031       |      1 |              1 |
| [187](#event-187)     | 0x0032       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x2F48      |       12104 |

## String References

- **12104**: Even if the city is invaded by beastmen, the Victory Gate alone must be defended to the last. It has been the pride of San d'Oria for generations! It must not fall!

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

### Event 605

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 41 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 66 00  80 F4 01 05 01 F4 01 05   .....f.........
0010: 01 74 6C 6B 30 1D 01 80  23 66 00 80 F4 01 05 01  .tlk0...#f......
0020: F4 01 05 01 74 6C 6B 31  21 00                    ....tlk1!.      
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Touttaures (ID: 17105396/0x010501F4), Touttaures (ID: 17105396/0x010501F4)], work=20*
  2: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=12104*)
    → "Even if the city is invaded by beastmen, the Victory Gate alone must be defended to the last. It has been the pride of San d'Oria for generations! It must not fall!"
  3: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0019 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Touttaures (ID: 17105396/0x010501F4), Touttaures (ID: 17105396/0x010501F4)], work=20*
  5: 0x0028 [0x21] END_EVENT
  6: 0x0029 [0x00] END_REQSTACK()
```

### Event 55

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                00                           .     
```

#### Opcodes

```
  0: 0x002A [0x00] END_REQSTACK()
```

### Event 86

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   00                         .    
```

#### Opcodes

```
  0: 0x002B [0x00] END_REQSTACK()
```

### Event 87

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      00                       .   
```

#### Opcodes

```
  0: 0x002C [0x00] END_REQSTACK()
```

### Event 89

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         00                     .  
```

#### Opcodes

```
  0: 0x002D [0x00] END_REQSTACK()
```

### Event 123

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            00                   . 
```

#### Opcodes

```
  0: 0x002E [0x00] END_REQSTACK()
```

### Event 127

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

### Event 148

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0030  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0030 [0x00] END_REQSTACK()
```

### Event 186

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0031  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    00                                              .              
```

#### Opcodes

```
  0: 0x0031 [0x00] END_REQSTACK()
```

### Event 187

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0032  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       00                                            .             
```

#### Opcodes

```
  0: 0x0032 [0x00] END_REQSTACK()
```
