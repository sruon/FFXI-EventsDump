# 17162747 - Uricca-Koricca

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 116 bytes                    |
| Total Events     | 4                            |
| References Count | 5                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [437](#event-437)     | 0x0001       |     30 |              8 |
| [222](#event-222)     | 0x001F       |     30 |              8 |
| [153](#event-153)     | 0x003D       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x2AE8      |       10984 |
|       2 | 0x2AE9      |       10985 |
|       3 | 0x2AF0      |       10992 |
|       4 | 0x2AF1      |       10993 |

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

### Event 437

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F8 FF FF 7F F0 FF  FF 7F 1C 00 80 2B F8 FF   J...........+..
0010: FF 7F 01 80 23 2B F8 FF  FF 7F 02 80 23 21 00     ....#+......#!. 
```

#### Opcodes

```
  0: 0x0001 [0x4A] EventEntity looks at LocalPlayer
  1: 0x000A [0x1C] WAIT(30* ticks)
  2: 0x000D [0x2B] EventEntity [10984*]:
    → "A while ago my brother joined the War Warlocks."
  3: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0015 [0x2B] EventEntity [10985*]:
    → "Even though I'm proud that he is one of the warlock elitaru, I can't help but worry if he's alright or not...<sigh>."
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x21] END_EVENT
  7: 0x001E [0x00] END_REQSTACK()
```

### Event 222

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               4A                 J
0020: F8 FF FF 7F F0 FF FF 7F  1C 00 80 2B F8 FF FF 7F  ...........+....
0030: 03 80 23 2B F8 FF FF 7F  04 80 23 21 00           ..#+......#!.   
```

#### Opcodes

```
  0: 0x001F [0x4A] EventEntity looks at LocalPlayer
  1: 0x0028 [0x1C] WAIT(30* ticks)
  2: 0x002B [0x2B] EventEntity [10992*]:
    → "My mommy told me to run to Windurst Walls before the scary-wary monsters come, but I forgotaru how to get there!"
  3: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0033 [0x2B] EventEntity [10993*]:
    → "But it's okay! My brother will keep us safe. He's a big-time War Warlock, you know!"
  5: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x003B [0x21] END_EVENT
  7: 0x003C [0x00] END_REQSTACK()
```

### Event 153

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         00                     .  
```

#### Opcodes

```
  0: 0x003D [0x00] END_REQSTACK()
```
