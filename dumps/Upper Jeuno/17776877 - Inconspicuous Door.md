# 17776877 - Inconspicuous Door

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 268 bytes             |
| Total Events     | 5                     |
| References Count | 14                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [10186](#event-10186) | 0x0001       |     47 |             13 |
| [10187](#event-10187) | 0x0030       |     47 |             13 |
| [10188](#event-10188) | 0x005F       |     47 |             13 |
| [10189](#event-10189) | 0x008E       |     34 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x3053      |       12371 |
|       1 | 0x3054      |       12372 |
|       2 | 0x0470      |        1136 |
|       3 | 0x3055      |       12373 |
|       4 | 0x3051      |       12369 |
|       5 | 0x3052      |       12370 |
|       6 | 0x0471      |        1137 |
|       7 | 0x3056      |       12374 |
|       8 | 0x305A      |       12378 |
|       9 | 0x0472      |        1138 |
|      10 | 0x3057      |       12375 |
|      11 | 0x3062      |       12386 |
|      12 | 0x30C9      |       12489 |
|      13 | 0x30CA      |       12490 |

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

### Event 10186

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 47 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    2B E0 40 0F 01 00 80  23 2B E0 40 0F 01 01 80   +.@....#+.@....
0010: 23 03 02 10 02 80 2B E0  40 0F 01 03 80 23 2B E0  #.....+.@....#+.
0020: 40 0F 01 04 80 23 2B E0  40 0F 01 05 80 23 21 00  @....#+.@....#!.
```

#### Opcodes

```
  0: 0x0001 [0x2B] Moogle (ID: 17776864/0x010F40E0) [12371*]:
    → "Yes, Master?"
  1: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0009 [0x2B] Moogle (ID: 17776864/0x010F40E0) [12372*]:
    → "I'm all tied up making repairs at the moment. Do forgive me, kupo!"
  3: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0011 [0x03] Work_Zone[2] = 1136*
  5: 0x0016 [0x2B] Moogle (ID: 17776864/0x010F40E0) [12373*]:
    → "By the way, have you been able to track down that $3 yet? Please, Master! Only you can restore structural soundness to your home sweet home!"
  6: 0x001D [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001E [0x2B] Moogle (ID: 17776864/0x010F40E0) [12369*]:
    → "An adventurer with your mining mastery should be able to find it in a flash, kupo! You wouldn't object to obtaining it for me, would you?"
  8: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0026 [0x2B] Moogle (ID: 17776864/0x010F40E0) [12370*]:
    → "While you're out, I'll take up my tools and get cracking. Happy hunting!"
 10: 0x002D [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x002E [0x21] END_EVENT
 12: 0x002F [0x00] END_REQSTACK()
```

### Event 10187

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 47 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 2B E0 40 0F 01 00 80 23  2B E0 40 0F 01 01 80 23  +.@....#+.@....#
0040: 03 02 10 06 80 2B E0 40  0F 01 07 80 23 2B E0 40  .....+.@....#+.@
0050: 0F 01 08 80 23 2B E0 40  0F 01 05 80 23 21 00     ....#+.@....#!. 
```

#### Opcodes

```
  0: 0x0030 [0x2B] Moogle (ID: 17776864/0x010F40E0) [12371*]:
    → "Yes, Master?"
  1: 0x0037 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0038 [0x2B] Moogle (ID: 17776864/0x010F40E0) [12372*]:
    → "I'm all tied up making repairs at the moment. Do forgive me, kupo!"
  3: 0x003F [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0040 [0x03] Work_Zone[2] = 1137*
  5: 0x0045 [0x2B] Moogle (ID: 17776864/0x010F40E0) [12374*]:
    → "By the way, have you been able to track down that $3 yet? Please, Master! Only you can restore structural soundness to your home sweet home!"
  6: 0x004C [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x004D [0x2B] Moogle (ID: 17776864/0x010F40E0) [12378*]:
    → "You should be able to log it somewhere, I think."
  8: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0055 [0x2B] Moogle (ID: 17776864/0x010F40E0) [12370*]:
    → "While you're out, I'll take up my tools and get cracking. Happy hunting!"
 10: 0x005C [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x005D [0x21] END_EVENT
 12: 0x005E [0x00] END_REQSTACK()
```

### Event 10188

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 47 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               2B                 +
0060: E0 40 0F 01 00 80 23 2B  E0 40 0F 01 01 80 23 03  .@....#+.@....#.
0070: 02 10 09 80 2B E0 40 0F  01 0A 80 23 2B E0 40 0F  ....+.@....#+.@.
0080: 01 0B 80 23 2B E0 40 0F  01 05 80 23 21 00        ...#+.@....#!.  
```

#### Opcodes

```
  0: 0x005F [0x2B] Moogle (ID: 17776864/0x010F40E0) [12371*]:
    → "Yes, Master?"
  1: 0x0066 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0067 [0x2B] Moogle (ID: 17776864/0x010F40E0) [12372*]:
    → "I'm all tied up making repairs at the moment. Do forgive me, kupo!"
  3: 0x006E [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x006F [0x03] Work_Zone[2] = 1138*
  5: 0x0074 [0x2B] Moogle (ID: 17776864/0x010F40E0) [12375*]:
    → "By the way, have you been able to track down that $3 yet? Please, Master! Only you can restore structural soundness to your home sweet home!"
  6: 0x007B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x007C [0x2B] Moogle (ID: 17776864/0x010F40E0) [12386*]:
    → "Don't worry. Preoccupied predators are leaving their hard-earned catches all over the place these days. Succulent slabs of meat are literally lying around waiting to be harvested by a keen-eyed adventurer like yourself!"
  8: 0x0083 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0084 [0x2B] Moogle (ID: 17776864/0x010F40E0) [12370*]:
    → "While you're out, I'll take up my tools and get cracking. Happy hunting!"
 10: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x008C [0x21] END_EVENT
 12: 0x008D [0x00] END_REQSTACK()
```

### Event 10189

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008E   |
| Data Size    | 34 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                            2B E0                +.
0090: 40 0F 01 00 80 23 2B E0  40 0F 01 01 80 23 2B E0  @....#+.@....#+.
00A0: 40 0F 01 0C 80 23 2B E0  40 0F 01 0D 80 23 21 00  @....#+.@....#!.
```

#### Opcodes

```
  0: 0x008E [0x2B] Moogle (ID: 17776864/0x010F40E0) [12371*]:
    → "Yes, Master?"
  1: 0x0095 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0096 [0x2B] Moogle (ID: 17776864/0x010F40E0) [12372*]:
    → "I'm all tied up making repairs at the moment. Do forgive me, kupo!"
  3: 0x009D [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x009E [0x2B] Moogle (ID: 17776864/0x010F40E0) [12489*]:
    → "Oh, the agony! Oh, how it pains my tender moogle heart! But we have no choice, kupo..."
  5: 0x00A5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00A6 [0x2B] Moogle (ID: 17776864/0x010F40E0) [12490*]:
    → "I beg of you, Master. You must hop on your chocobo, make your way for [La Theine Plateau/Valkurm Dunes/Jugner Forest/Konschtat Highlands/Pashhow Marshlands/Tahrongi Canyon/Buburimu Peninsula/Meriphataud Mountains/The Sanctuary of Zi'Tah/Yuhtunga Jungle/Yhoator Jungle/Western Altepa Desert/Eastern Altepa Desert], and dig up my nest egg, kupo."
  7: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00AE [0x21] END_EVENT
  9: 0x00AF [0x00] END_REQSTACK()
```
