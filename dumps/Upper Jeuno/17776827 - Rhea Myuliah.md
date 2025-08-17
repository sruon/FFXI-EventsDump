# 17776827 - Rhea Myuliah

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 304 bytes             |
| Total Events     | 29                    |
| References Count | 15                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10121](#event-10121)    | 0x0001       |      6 |              4 |
| [10111](#event-10111)    | 0x0007       |      1 |              1 |
| [10114](#event-10114)    | 0x0008       |     11 |              5 |
| [10116](#event-10116)    | 0x0013       |      6 |              4 |
| [10117](#event-10117)    | 0x0019       |     15 |              7 |
| [10118](#event-10118)    | 0x0028       |      1 |              1 |
| [10126](#event-10126)    | 0x0029       |      6 |              4 |
| [65535.1](#event-655351) | 0x002F       |      3 |              2 |
| [65535.2](#event-655352) | 0x0032       |      3 |              2 |
| [112](#event-112)        | 0x0035       |      1 |              1 |
| [10129](#event-10129)    | 0x0036       |      1 |              1 |
| [10132](#event-10132)    | 0x0037       |     10 |              6 |
| [10135](#event-10135)    | 0x0041       |      6 |              4 |
| [10136](#event-10136)    | 0x0047       |      1 |              1 |
| [10138](#event-10138)    | 0x0048       |      6 |              4 |
| [10139](#event-10139)    | 0x004E       |      1 |              1 |
| [10141](#event-10141)    | 0x004F       |      6 |              4 |
| [10145](#event-10145)    | 0x0055       |      6 |              4 |
| [10147](#event-10147)    | 0x005B       |      1 |              1 |
| [10151](#event-10151)    | 0x005C       |      1 |              1 |
| [10209](#event-10209)    | 0x005D       |      1 |              1 |
| [10211](#event-10211)    | 0x005E       |      1 |              1 |
| [10149](#event-10149)    | 0x005F       |      1 |              1 |
| [10155](#event-10155)    | 0x0060       |      6 |              4 |
| [10160](#event-10160)    | 0x0066       |      1 |              1 |
| [10165](#event-10165)    | 0x0067       |      6 |              4 |
| [10172](#event-10172)    | 0x006D       |      1 |              1 |
| [10221](#event-10221)    | 0x006E       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2E28      |       11816 |
|       1 | 0x038F      |         911 |
|       2 | 0x2E2E      |       11822 |
|       3 | 0x2E35      |       11829 |
|       4 | 0x2E32      |       11826 |
|       5 | 0x2E33      |       11827 |
|       6 | 0x2E4C      |       11852 |
|       7 | 0x2E65      |       11877 |
|       8 | 0x2E62      |       11874 |
|       9 | 0x2E79      |       11897 |
|      10 | 0x2E88      |       11912 |
|      11 | 0x2EC5      |       11973 |
|      12 | 0x2ED7      |       11991 |
|      13 | 0x2F44      |       12100 |
|      14 | 0x2F5D      |       12125 |

## String References

- **11816**: I began studying here after one of Laila's performances moved me to tears. Such grrrace...such talent...
- **11822**: If you have the courrrage to dance on the stage in the Lion Springs Tavern, I'll ask Laila about that $3.
- **11826**: Twenty years ago, $5 could be found lying at the bottom of Lake Mechieume in Jugner Forest.
- **11827**: But their dazzling glow made them such a collector's item that not a single one remains there today.
- **11829**: It's a shame. While you still lack the skill, you certainly have the spirit of a dancer...
- **11852**: I'm glad you've joined our little grrroup, but be warned: the hard work has only just begun!
- **11874**: During the Great War, Witchfire Glen was rumored to be a mystical place, where pixies could be seen frolicking.
- **11877**: Laila's mother selected only the most talented dancers, and trrrained them at Witchfire Glen, in Grauberg.
- **11897**: I wonder why she's gotten cranky all of a sudden...
- **11912**: I wish I could meet a splendid musician who could strrrum on my heartstrings.
- **11973**: I never knew Laila had crossed paths with Troupe Valeriano in the past...
- **11991**: Why did Laila agrrree to a collaboration? I thought she didn't like Troupe Valeriano...
- **12100**: I will strrrive to become a great dancer like Laila.
- **12125**: Prrromise me you'll come back to dance with us again, <Player>.

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

### Event 10121

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 21 00                               ...#!.         
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=11816*)
    → "I began studying here after one of Laila's performances moved me to tears. Such grrrace...such talent..."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x21] END_EVENT
  3: 0x0006 [0x00] END_REQSTACK()
```

### Event 10111

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0007  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      00                                  .        
```

#### Opcodes

```
  0: 0x0007 [0x00] END_REQSTACK()
```

### Event 10114

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          03 02 10 01 80 1D 02 80          ........
0010: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0008 [0x03] Work_Zone[2] = 911*
  1: 0x000D [0x1D] PRINT_EVENT_MESSAGE(message_id=11822*)
    → "If you have the courrrage to dance on the stage in the Lion Springs Tavern, I'll ask Laila about that $3."
  2: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0011 [0x21] END_EVENT
  4: 0x0012 [0x00] END_REQSTACK()
```

### Event 10116

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0013  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          1D 03 80 23 21  00                          ...#!.       
```

#### Opcodes

```
  0: 0x0013 [0x1D] PRINT_EVENT_MESSAGE(message_id=11829*)
    → "It's a shame. While you still lack the skill, you certainly have the spirit of a dancer..."
  1: 0x0016 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0017 [0x21] END_EVENT
  3: 0x0018 [0x00] END_REQSTACK()
```

### Event 10117

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             03 02 10 01 80 1D 04           .......
0020: 80 23 1D 05 80 23 21 00                           .#...#!.        
```

#### Opcodes

```
  0: 0x0019 [0x03] Work_Zone[2] = 911*
  1: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=11826*)
    → "Twenty years ago, $5 could be found lying at the bottom of Lake Mechieume in Jugner Forest."
  2: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=11827*)
    → "But their dazzling glow made them such a collector's item that not a single one remains there today."
  4: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0026 [0x21] END_EVENT
  6: 0x0027 [0x00] END_REQSTACK()
```

### Event 10118

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0028  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          00                               .       
```

#### Opcodes

```
  0: 0x0028 [0x00] END_REQSTACK()
```

### Event 10126

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             1D 06 80 23 21 00              ...#!. 
```

#### Opcodes

```
  0: 0x0029 [0x1D] PRINT_EVENT_MESSAGE(message_id=11852*)
    → "I'm glad you've joined our little grrroup, but be warned: the hard work has only just begun!"
  1: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x002D [0x21] END_EVENT
  3: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002F  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               61                 a
0030: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x002F [0x61] EventEntity->Render.Flags2 |= 0x00000001
  1: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0032  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       61 00 00                                      a..           
```

#### Opcodes

```
  0: 0x0032 [0x61] EventEntity->Render.Flags2 &= ~0x00000001
  1: 0x0034 [0x00] END_REQSTACK()
```

### Event 112

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0035  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                00                                      .          
```

#### Opcodes

```
  0: 0x0035 [0x00] END_REQSTACK()
```

### Event 10129

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0036  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   00                                    .         
```

#### Opcodes

```
  0: 0x0036 [0x00] END_REQSTACK()
```

### Event 10132

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 10 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      1D  07 80 23 1D 08 80 23 21         ...#...#!
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=11877*)
    → "Laila's mother selected only the most talented dancers, and trrrained them at Witchfire Glen, in Grauberg."
  1: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x003B [0x1D] PRINT_EVENT_MESSAGE(message_id=11874*)
    → "During the Great War, Witchfire Glen was rumored to be a mystical place, where pixies could be seen frolicking."
  3: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x003F [0x21] END_EVENT
  5: 0x0040 [0x00] END_REQSTACK()
```

### Event 10135

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0041  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    1D 09 80 23 21 00                               ...#!.         
```

#### Opcodes

```
  0: 0x0041 [0x1D] PRINT_EVENT_MESSAGE(message_id=11897*)
    → "I wonder why she's gotten cranky all of a sudden..."
  1: 0x0044 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0045 [0x21] END_EVENT
  3: 0x0046 [0x00] END_REQSTACK()
```

### Event 10136

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0047  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      00                                  .        
```

#### Opcodes

```
  0: 0x0047 [0x00] END_REQSTACK()
```

### Event 10138

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0048  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          1D 0A 80 23 21 00                ...#!.  
```

#### Opcodes

```
  0: 0x0048 [0x1D] PRINT_EVENT_MESSAGE(message_id=11912*)
    → "I wish I could meet a splendid musician who could strrrum on my heartstrings."
  1: 0x004B [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x004C [0x21] END_EVENT
  3: 0x004D [0x00] END_REQSTACK()
```

### Event 10139

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            00                   . 
```

#### Opcodes

```
  0: 0x004E [0x00] END_REQSTACK()
```

### Event 10141

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004F  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               1D                 .
0050: 0B 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=11973*)
    → "I never knew Laila had crossed paths with Troupe Valeriano in the past..."
  1: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0053 [0x21] END_EVENT
  3: 0x0054 [0x00] END_REQSTACK()
```

### Event 10145

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0055  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                1D 0C 80  23 21 00                      ...#!.     
```

#### Opcodes

```
  0: 0x0055 [0x1D] PRINT_EVENT_MESSAGE(message_id=11991*)
    → "Why did Laila agrrree to a collaboration? I thought she didn't like Troupe Valeriano..."
  1: 0x0058 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0059 [0x21] END_EVENT
  3: 0x005A [0x00] END_REQSTACK()
```

### Event 10147

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   00                         .    
```

#### Opcodes

```
  0: 0x005B [0x00] END_REQSTACK()
```

### Event 10151

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      00                       .   
```

#### Opcodes

```
  0: 0x005C [0x00] END_REQSTACK()
```

### Event 10209

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         00                     .  
```

#### Opcodes

```
  0: 0x005D [0x00] END_REQSTACK()
```

### Event 10211

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            00                   . 
```

#### Opcodes

```
  0: 0x005E [0x00] END_REQSTACK()
```

### Event 10149

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               00                 .
```

#### Opcodes

```
  0: 0x005F [0x00] END_REQSTACK()
```

### Event 10155

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0060  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 1D 0D 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x0060 [0x1D] PRINT_EVENT_MESSAGE(message_id=12100*)
    → "I will strrrive to become a great dancer like Laila."
  1: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0064 [0x21] END_EVENT
  3: 0x0065 [0x00] END_REQSTACK()
```

### Event 10160

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0066  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   00                                    .         
```

#### Opcodes

```
  0: 0x0066 [0x00] END_REQSTACK()
```

### Event 10165

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0067  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      1D  0E 80 23 21 00                  ...#!.   
```

#### Opcodes

```
  0: 0x0067 [0x1D] PRINT_EVENT_MESSAGE(message_id=12125*)
    → "Prrromise me you'll come back to dance with us again, <Player>."
  1: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x006B [0x21] END_EVENT
  3: 0x006C [0x00] END_REQSTACK()
```

### Event 10172

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         00                     .  
```

#### Opcodes

```
  0: 0x006D [0x00] END_REQSTACK()
```

### Event 10221

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            00                   . 
```

#### Opcodes

```
  0: 0x006E [0x00] END_REQSTACK()
```
