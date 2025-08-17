# 17105397 - Sabiliont

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 84 bytes                         |
| Total Events     | 6                                |
| References Count | 3                                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [608](#event-608)     | 0x0001       |     15 |              7 |
| [27](#event-27)       | 0x0010       |     12 |              6 |
| [129](#event-129)     | 0x001C       |      1 |              1 |
| [133](#event-133)     | 0x001D       |      1 |              1 |
| [139](#event-139)     | 0x001E       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2F4A      |       12106 |
|       1 | 0x2F4B      |       12107 |
|       2 | 0x2ACB      |       10955 |

## String References

- **10955**: A charm from the Young Griffons? Splendid! I shall wear it into battle with pride. Send my thanks to those thoughtful lads!
- **12106**: That rich, black plumage. Those sturdy, sure legs. Not like those scrawny green and blue chocobos you see the other nations turning out, huh?
- **12107**: San d'Orian chocobos are of the finest breeding. It goes without saying that our birds are far superior to those of Windurst and Bastok.

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

### Event 608

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 21 00   ........#...#!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=12106*)
    → "That rich, black plumage. Those sturdy, sure legs. Not like those scrawny green and blue chocobos you see the other nations turning out, huh?"
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=12107*)
    → "San d'Orian chocobos are of the finest breeding. It goes without saying that our birds are far superior to those of Windurst and Bastok."
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x21] END_EVENT
  6: 0x000F [0x00] END_REQSTACK()
```

### Event 27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 12 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 42 1E F0 FF FF 7F 1D 02  80 23 21 00              B........#!.    
```

#### Opcodes

```
  0: 0x0010 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0011 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0016 [0x1D] PRINT_EVENT_MESSAGE(message_id=10955*)
    → "A charm from the Young Griffons? Splendid! I shall wear it into battle with pride. Send my thanks to those thoughtful lads!"
  3: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x001A [0x21] END_EVENT
  5: 0x001B [0x00] END_REQSTACK()
```

### Event 129

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      00                       .   
```

#### Opcodes

```
  0: 0x001C [0x00] END_REQSTACK()
```

### Event 133

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         00                     .  
```

#### Opcodes

```
  0: 0x001D [0x00] END_REQSTACK()
```

### Event 139

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            00                   . 
```

#### Opcodes

```
  0: 0x001E [0x00] END_REQSTACK()
```
